from application.modules.cor.Handler import Handler
from infrastructure.SocketIoClient import SocketIoClient
from constants.constants import UNNAVIGATOR_INTENT

class PageNavigatorHandler(Handler):
    def __init__(self):
        self.sio = SocketIoClient()
    def handle(self, state)->bool:
        intent = state["intent"]
        if intent not in UNNAVIGATOR_INTENT:
            intent = intent.replace(" ","-")
            self.sio.instance.emit("navigateCommand",f"/{intent}")
            return super().handle(state)
        return super().handle(state)