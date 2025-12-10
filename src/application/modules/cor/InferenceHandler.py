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
            * If user mentions an exact day (e.g., Monday, Tuesday, Rabu, Jumat, "on Friday", "tanggal 12") → use intent with 'specific day'.
            * If user only says 'daily','today','this day', 'every day', 'harian' without naming a specific day → use intent with 'today' or 'daily' depending on available intents.

            - WEEK:
            * If user mentions an exact week (e.g., "next week", "week of 12th", "minggu depan") → use intent with 'specific week'.
            * If user only says 'weekly','this week',' 'every week', 'mingguan' without naming a specific week → use intent with 'weekly'.

            - MONTH:
            * If user mentions an exact month (e.g., January, February, March, "bulan Maret", "next month") → use intent with 'specific month'.
            * If user only says 'monthly', 'every month','this month',' 'bulanan' without naming a specific month → use intent with 'monthly'.

            - If no clear match → 'other topics'.

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