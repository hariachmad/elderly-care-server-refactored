from application.modules.lang_graph.Workflow import Workflow
from application.modules.lang_graph.Graph import Graph
class GraphBuilder:
    def __init__(self):
        self.workflow : Workflow = None
    
    def set_workflow(self, workflow):
        self.workflow = workflow
        return self
    
    def build(self):
        return Graph(self.workflow.instance.compile())