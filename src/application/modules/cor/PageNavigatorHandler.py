from application.modules.cor.Handler import Handler
from infrastructure.SocketIoClient import SocketIoClient
from constants.UnnavigatorIntent import UNNAVIGATOR_INTENT
from constants.IntentToNode import INTENT_TO_NODE

class PageNavigatorHandler(Handler):
    def __init__(self):
        self.sio = SocketIoClient()
        super().__init__()
    def handle(self, state)->bool:
        intent = state["intent"]
        path = INTENT_TO_NODE[intent]
        for key in state["date"]:
            path = path+"/"+str(state["date"][key])
        if intent not in UNNAVIGATOR_INTENT:
            self.sio.instance.emit("navigateCommand",f"/{path}")
            if super().handle(state) is None:
                return state
            return super().handle(state)
        if super().handle(state) is None:
                return state
        return super().handle(state)