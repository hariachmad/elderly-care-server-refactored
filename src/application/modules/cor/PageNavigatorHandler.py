from application.modules.cor.Handler import Handler
from infrastructure.SocketIoClient import SocketIoClient
import socketio
class PageNavigatorHandler(Handler):
    def __init__(self):
        self.sio = SocketIoClient()
    def handle(self, answer)->bool:
        intent = answer["intent"]
        intent = intent.replace(" ","-")
        self.sio.instance.emit("navigateCommand",f"/{intent}")