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
            template="""You are an advanced intent classifier for a healthcare assistant system.
        
        Your task is to classify the user's query into the most appropriate intent from the provided list.
        
        IMPORTANT CONTEXT:
        - This system is used by elderly patients for managing their health schedule.
        - Always consider the context of medicine, appointments, activities, and device control.
        - Be precise with time references: "today", "tomorrow", specific dates, or relative time periods.
        
        AVAILABLE INTENTS:
        {intents}
        
        USER'S QUERY:
        {user_input}
        
        INSTRUCTIONS:
        1. Analyze the query carefully.
        2. Match the query to the most specific intent possible.
        3. Consider synonyms and similar phrasings.
        4. If the query doesn't clearly match any intent, choose "other topics".
        5. Pay special attention to time references (today, weekly, monthly, specific dates).
        
        {format_instructions}
        
        EXAMPLES FOR REFERENCE:
        - "What medicine should I take today?" → medicine schedule today
        - "Show my doctor appointments next week" → doctor appointment schedule specific week
        - "Turn up the brightness" → Increase Screen's Brightness
        - "Help!" → help
        """,
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