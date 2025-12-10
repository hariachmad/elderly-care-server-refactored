from application.modules.cor.Handler import Handler
from application.modules.ai_agent.AiAgentBuilder import AiAgentBuilder
from application.modules.lang_graph.Node import Node
from application.modules.lang_graph.WorkflowBuilder import WorkflowBuilder
from application.modules.lang_graph.GraphBuilder import GraphBuilder
from application.modules.lang_graph.AnswerBuilder import AnswerBuilder
from constants.MedicalKeywords import medical_keywords
from constants.PredefinedIntents import predefined_intents
from constants.NodeConfigs import node_configs
from utils.utils import date_time_invoker
from infrastructure.LlmClient import LlmClient
import os
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

class InferenceHandler(Handler):
    def handle(self,input)->bool:
        load_dotenv()     
        response_schemas = [
        ResponseSchema(
            name="intent",
            description=(
                f"The user's intent. Allowed values: {predefined_intents}. "
                "If input is empty, unclear, incomplete, not meaningful, or does not correspond YOU MUST return 'other'"
                "to any known intent, YOU MUST return 'other'. "
                "Never guess. Only classify when confident."
            )
        )
        ]
        parser = StructuredOutputParser.from_response_schemas(response_schemas)
        # prompt = PromptTemplate(
        #         template="""You are an intent classifier.
        #     Choose the most appropriate intent from the following list:
        #     {intents}

        #     User input: {user_input}

        #     {format_instructions}""",
        #         input_variables=["intents", "user_input"],
        #         partial_variables={
        #             "format_instructions": parser.get_format_instructions(),
        #         }
        #     )

        prompt = PromptTemplate(
    template="""You are an intent classifier.
Choose the most appropriate intent from the following list:
{intents}

User input: {user_input}

RULES:
- DAY:
  * If user mentions an exact day name (e.g., Monday, Tuesday, Rabu, Jumat) or a specific date (e.g., "on 12th", "tanggal 5") → use intent with 'specific day'.

- WEEK:
  * If user mentions "week", "week X", "week number", "minggu ke-X", 
    "minggu depan", "next week", "this week", "week of <date>" 
    → classify as 'weekly'.
  * If user mentions a week combined with a month or year 
    (e.g., "third week of January", "minggu pertama 2026")
    → still classify as 'weekly'.
  * A week NEVER counts as a specific day.
  * There is NO 'specific week' intent, so always use 'weekly'.

- MONTH:
  * If user mentions an exact month name (January, February, Maret, etc.)
    OR a month combined with a year (e.g., "January 2026", "Maret 2024")
    → use intent with 'monthly'.
  * Do NOT classify month references as 'specific day'.
  * Only use 'monthly' because 'specific month' is not available in predefined intents.

- ACTIVITY TYPE:
  * HEALTH ACTIVITY:
      - Activities involving exercise or physical movement.
      - Examples: yoga, ballroom dance, gym, aerobics, pilates, stretching, tai chi.
  * SOCIAL ACTIVITY:
      - Activities focused on social interaction, games, or entertainment.
      - Examples: bingo, board games, card games, chess, trivia night, movie night.

- If the user mentions an activity, classify based on these definitions.

- If no clear match → 'other topics'.

- VISIT vs DOCTOR APPOINTMENT:

  * doctor appointment:
    - If the visitor is a medical professional:
      * doctor / dokter
      * nurse / perawat
      * caregiver
      * physiotherapist / fisioterapis
      * therapist
      * medical staff / tenaga medis
    → classify as 'doctor appointment'.

  * visit except doctor:
    - If the visitor is NOT a medical professional:
      * family (keluarga)
      * friends (teman)
      * neighbors (tetangga)
      * volunteers
      * guests
      * general visitors
    → classify as 'visit except doctor'.

  * If the visitor is ambiguous and no clear indication of medical role:
    → default to 'visit except doctor'.

INSTRUCTIONS:
1. Match the query to the most specific intent possible.
2. Consider synonyms and similar phrasings (e.g., "mingguan" → weekly, "bulanan" → monthly, "harian" → specific day).
3. Output MUST be one of the intents listed above.

{format_instructions}""",
    input_variables=["intents", "user_input"],
    partial_variables={
        "format_instructions": parser.get_format_instructions(),
    }
)

        model = os.getenv("LLM_MODEL")
        temperature = int(os.getenv("LLM_TEMPERATURE", "0"))
        base_url = os.getenv("LLM_BASE_URL", "http://localhost:11434/")
        llm = LlmClient(model, temperature, base_url).instance
        dt_entities = date_time_invoker(llm,input)
        aiAgent = AiAgentBuilder().set_predefined_intents(predefined_intents).set_blacklist_keywords(medical_keywords).set_prompt_template(prompt).set_llm(llm).set_parser(parser).build()
        node = Node(predefined_intents, aiAgent.chain, dt_entities)
        workflow = WorkflowBuilder().set_nodes(node).set_node_configs(node_configs).build()
        graph = GraphBuilder().set_workflow(workflow).build()
        answer = graph.instance.invoke({"intents": predefined_intents,"user_input": input})
        result = AnswerBuilder().set_llm(llm).set_answer(answer).set_ask_llm_answers(["asking again"]).build()
        if super().handle(result) is None:
            return result
        return super().handle(result)