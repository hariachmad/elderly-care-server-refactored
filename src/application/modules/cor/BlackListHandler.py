from application.modules.cor.Handler import Handler
from utils.utils import blacklist_keyword_guard
from constants.constants import medical_keywords
from application.modules.lang_graph.State import State

class BlackListHandler(Handler):
    def handle(self, prompt)->bool:
        if not blacklist_keyword_guard(medical_keywords,prompt):
            return super().handle(prompt)
        return State(final_answer="I'm sorry, I can't help you with that.")