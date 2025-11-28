from application.modules.cor.Handler import Handler
from utils.utils import blacklist_keyword_guard
from constants.constants import medical_keywords
from application.modules.lang_graph.State import State
from application.modules.cor.AudioFileDispatcherHandler import AudioFileDispatcherHandler

class BlackListHandler(Handler):
    def handle(self, prompt)->bool:
        audioFileDispatcher = AudioFileDispatcherHandler()
        if not blacklist_keyword_guard(medical_keywords,prompt):
            return super().handle(prompt)
        audioFileDispatcher.handle(State(final_answer="I'm sorry, I can't help you with that."))