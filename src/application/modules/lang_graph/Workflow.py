from langgraph.graph import StateGraph
from application.modules.lang_graph.Node import Node
class Workflow:
    def __init__(self, nodes : Node, workflow : StateGraph):
        self.nodes : Node = nodes
        self.instance : StateGraph = workflow