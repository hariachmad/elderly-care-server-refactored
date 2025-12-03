from application.modules.lang_graph.State import State
from langchain_ollama import OllamaEmbeddings
from langchain_classic.vectorstores import FAISS
class Node:
    def __init__(self, predefined_intents, chain,entities):
        self.predefined_intents = predefined_intents
        self.chain = chain
        self.entities = entities
    
    def classify_intent_node(self,state:State):
        # embeddings = OllamaEmbeddings( model="qwen2.5:7b",
        # base_url="http://localhost:11434/", )
        # vectorstore = FAISS.from_texts(self.predefined_intents, embeddings)

        # docs = vectorstore.similarity_search_with_score(state["user_input"], k=1)
        # doc, score = docs[0]
        # if score > 1.0:
        #     return {
        #         "intent": 'other',
        #         "entities" : self.entities
        #     }     
        # else :
        #     return {
        #         "intent": doc.page_content,
        #         "entities" : self.entities
        #     } 
        result = self.chain.invoke({"user_input": state["user_input"],
        "intents": self.predefined_intents})
        return {
            "intent": result["intent"],
            "entities" : self.entities
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
        if intent == "medicine schedule specific day":
            return "medicine_schedule_specific_day"
        
        # Doctor appointment related intents
        if intent == "doctor appointment schedule today":
            return "doctor_appointment_today"
        if intent == "doctor appointment schedule weekly":
            return "doctor_appointment_weekly"
        if intent == "doctor appointment schedule monthly":
            return "doctor_appointment_monthly"
        if intent == "doctor appointment schedule specific day":
            return "doctor_appointment_specific_day"
        
        # Social activity related intents
        if intent == "social activity schedule today":
            return "social_activity_today"
        if intent == "social activity schedule weekly":
            return "social_activity_weekly"
        if intent == "social activity schedule monthly":
            return "social_activity_monthly"
        if intent == "social activity schedule specific day":
            return "social_activity_specific_day"

        # Visit except doctor related intents
        if intent == "visit except doctor schedule today":
            return "visit_except_doctor_today"
        if intent == "visit except doctor schedule weekly":
            return "visit_except_doctor_weekly"
        if intent == "visit except doctor schedule monthly":
            return "visit_except_doctor_monthly"
        if intent == "visit except doctor schedule specific day":
            return "visit_except_doctor_specific_day"
        
        # Fall detection
        if intent == "i am ok":
            return "i_am_ok"
        if intent == "help":
            return "help"
        if intent == "fall":
            return "fall"

        return "final"

    