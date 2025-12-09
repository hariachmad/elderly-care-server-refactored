from application.modules.lang_graph.State import State
from constants.IntentToNode import INTENT_TO_NODE
class Node:
    def __init__(self, predefined_intents, chain,entities):
        self.predefined_intents = predefined_intents
        self.chain = chain
        self.entities = entities
    
    def classify_intent_node(self,state:State):
        result = self.chain.invoke({"user_input": state["user_input"],
        "intents": self.predefined_intents})
        return {
            "intent": result["intent"],
            "entities" : self.entities
        }

    
    def router_node(self, state: State):
        intent = state["intent"]
        return INTENT_TO_NODE.get(intent, "final")

    