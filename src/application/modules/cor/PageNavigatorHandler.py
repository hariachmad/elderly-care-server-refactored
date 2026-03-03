from application.modules.cor.Handler import Handler
from infrastructure.SocketIoClient import SocketIoClient
from constants.UnnavigatorIntent import UNNAVIGATOR_INTENT
from constants.IntentToNode import INTENT_TO_NODE
import json

class PageNavigatorHandler(Handler):
    def __init__(self):
        self.sio = SocketIoClient()
        super().__init__()
    def handle(self, state)->bool:
        path = None
        intent = state["intent"]
        node = INTENT_TO_NODE[intent]
        print("state: ",state)
        if state["date"]:
            if intent not in UNNAVIGATOR_INTENT:
                self.sio.instance.emit(node,json.dumps(state["date"]))
                if super().handle(state) is None:
                    return state
            return super().handle(state)
        if super().handle(state) is None:
                return state
        return super().handle(state)