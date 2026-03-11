from application.modules.cor.Handler import Handler
from utils.utils import blacklist_keyword_guard
from constants.MedicalKeywords import medical_keywords
from application.modules.lang_graph.State import State
from application.modules.cor.AudioFileDispatcherHandler import AudioFileDispatcherHandler
from utils.utils import translate

class BlackListHandler(Handler):
    def handle(self, prompt, lang="en")->bool:
        audioFileDispatcher = AudioFileDispatcherHandler()
        if not blacklist_keyword_guard(medical_keywords,prompt):
            return super().handle(prompt, lang)
        audioFileDispatcher.handle(State(final_answer=translate(lang,translate(lang,"blacklist_question"))))
        return translate(lang,"blacklist_question")