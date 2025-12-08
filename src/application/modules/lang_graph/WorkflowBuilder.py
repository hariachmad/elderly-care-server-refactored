from langgraph.graph import StateGraph, END
from application.modules.lang_graph.Node import Node
from application.modules.lang_graph.Workflow import Workflow
from application.modules.lang_graph.State import State
class WorkflowBuilder:
    def __init__(self): 
        self.nodes : Node = None
        self.node_configs = None
        self.workflow = StateGraph(State)
    
    def set_nodes(self, nodes : Node):
        self.nodes = nodes
        return self
    
    def set_node_configs(self, node_configs : dict[str, dict[str, str]]):
        self.node_configs = node_configs
        return self
    
    def build(self):
        if self.node_configs is None:
            raise ValueError("node_configs must be set")
        
        self.workflow.add_node("classify_intent", self.nodes.classify_intent_node)   
        
        for node_name, schedule_type in self.node_configs.items():
            self.workflow.add_node(
            node_name, 
            lambda state, st=schedule_type: {"final_answer": st["final_answer"]})
        
        self.workflow.add_node("router", lambda state: state)

        self.workflow.set_entry_point("classify_intent")

        self.workflow.add_edge("classify_intent", "router")
        
        routers = {}
        
        for node_name, schedule_type in self.node_configs.items():
            routers[node_name] = node_name
        
        self.workflow.add_conditional_edges(
        "router",
        self.nodes.router_node,
        routers 
        )

        for node_name, _ in self.node_configs.items():
            self.workflow.add_edge(node_name,END)
        
        self.workflow.add_edge("final", END)
    
        return Workflow(self.nodes, self.workflow)