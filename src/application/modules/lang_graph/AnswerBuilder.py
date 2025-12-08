class AnswerBuilder:
    def __init__(self):
        self.llm = None
        self.answer = None
        self.askLlmAnswers = []

    def set_answer(self, _answer):
        self.answer = _answer
        return self
    
    def set_llm(self, _llm):
        self.llm = _llm
        return self
    
    def set_ask_llm_answers(self, _askLlmAnswers):
        self.askLlmAnswers = _askLlmAnswers
        return self
    
    def build(self):
        if self.llm is None:
            raise ValueError("llm must be set")

        if len(self.askLlmAnswers) == 0:
            raise ValueError("askLlmAnswer must be set")
        
        if not self.answer:
            raise ValueError("answer must be set")
        
        if self.answer["final_answer"] in self.askLlmAnswers:
            self.answer["final_answer"] = self.llm.invoke(self.answer["final_answer"]).content
            return self.answer
        
        return self.answer