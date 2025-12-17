from application.modules.cor.Handler import Handler
from utils.utils import wake_word_guard
from constants.WakeWord import wake_words
from application.modules.lang_graph.State import State
from application.modules.cor.AudioFileDispatcherHandler import AudioFileDispatcherHandler

class WakeWordHandler(Handler):
    def handle(self, prompt)->bool:
        audioFileDispatcher = AudioFileDispatcherHandler()
        if not wake_word_guard(wake_words,prompt):
            return super().handle(prompt)
        audioFileDispatcher.handle(State(final_answer="Hi, what can I do for you?"))
        return "Hi, what can I do for you?"