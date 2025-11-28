import socketio
from dotenv import load_dotenv
import os

class SocketIoClient:
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SocketIoClient, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return  

        load_dotenv()
        self.instance = socketio.Client()
        self.instance.on("connect", self.on_connect)
        self.instance.on("disconnect", self.on_disconnect)
        self.instance.on("message", self.on_message)
        server_url = os.getenv("SOCKETIO_SERVER_URL", "http://localhost:3000")
        self.instance.connect(server_url)

        self._initialized = True
        
    def on_connect(self):
        print("Connected to Socket.IO server")
    
    def on_disconnect(self):
        print("Disconnected from Socket.IO server")
    
    def on_message(self, data):
        print("Message received:", data)
