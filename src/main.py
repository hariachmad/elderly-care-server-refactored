from dotenv import load_dotenv
from constants.constants import medical_keywords, predefined_intents, node_configs
import os
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
from infrastructure.LlmClient import LlmClient
from application.modules.ai_agent.AiAgentBuilder import AiAgentBuilder
from application.modules.lang_graph.Node import Node
from application.modules.lang_graph.State import State
from application.modules.lang_graph.WorkflowBuilder import WorkflowBuilder
from application.modules.lang_graph.Workflow import Workflow
from application.modules.ai_agent.AiAgent import AiAgent
from langchain_ollama import ChatOllama 
from application.modules.lang_graph.GraphBuilder import GraphBuilder
from utils.utils import date_time_invoker
from application.modules.cor.BlackListHandler import BlackListHandler

load_dotenv()
model = os.getenv("LLM_MODEL", "gemma2:2b")
temperature = int(os.getenv("LLM_TEMPERATURE", 0))
base_url = os.getenv("LLM_BASE_URL", "http://localhost:11434/")

llm = LlmClient(model, temperature, base_url).instance
response_schemas = [
    ResponseSchema(
        name="intent", 
        description=f"User's goal or action. MUST be exactly one of: {predefined_intents}. If no match, return 'other'"
    )
]
parser = StructuredOutputParser.from_response_schemas(response_schemas)
prompt = PromptTemplate(
    template="""You are an intent classifier.
Choose the most appropriate intent from the following list:
{intents}

User input: {user_input}

{format_instructions}""",
    input_variables=["intents", "user_input"],
    partial_variables={
        "format_instructions": parser.get_format_instructions(),
    }
)

userInput = "What is my medications schedule at tomorrow?"
dt_entities = date_time_invoker(llm,userInput)

blacklist = BlackListHandler()
result = blacklist.handle(userInput)
print(result)

aiAgent = AiAgentBuilder().set_predefined_intents(predefined_intents).set_blacklist_keywords(medical_keywords).set_prompt_template(prompt).set_llm(llm).set_parser(parser).build()
node = Node(predefined_intents, aiAgent.chain, dt_entities)
workflow = WorkflowBuilder().set_nodes(node).set_node_configs(node_configs).build()
graph = GraphBuilder().set_workflow(workflow).build()

answer = graph.instance.invoke({"user_input": userInput})
print(answer)
