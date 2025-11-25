from application.modules.lang_graph.State import State
class Node:
    def __init__(self, predefined_intents, chain):
        self.predefined_intents = predefined_intents
        self.chain = chain
    
    def classify_intent_node(self,state:State):
        result = self.chain.invoke({"user_input": state["user_input"],
        "intents": self.predefined_intents})
        return {
            "intent": result["intent"],
        }
    
    def router_node(self, state: State):
        intent = state["intent"]

        # Medicine related intents
        if intent == "medicine schedule today":
            return "medicine_today"
        if intent == "medicine schedule weekly":
            return "medicine_weekly" 
        if intent == "medicine schedule monthly":
            return "medicine_monthly"

        # Doctor appointment related intents
        if intent == "doctor appointment schedule today":
            return "doctor_appointment_today"
        if intent == "doctor appointment schedule weekly":
            return "doctor_appointment_weekly"
        if intent == "doctor appointment schedule monthly":
            return "doctor_appointment_monthly"

        # Social activity related intents
        if intent == "social activity schedule today":
            return "social_activity_today"
        if intent == "social activity schedule weekly":
            return "social_activity_weekly"
        if intent == "social activity schedule monthly":
            return "social_activity_monthly"

        # Visit except doctor related intents
        if intent == "visit except doctor schedule today":
            return "visit_except_doctor_today"
        if intent == "visit except doctor schedule weekly":
            return "visit_except_doctor_weekly"
        if intent == "visit except doctor schedule monthly":
            return "visit_except_doctor_monthly"

        return "final"

    