import socketio
from dotenv import load_dotenv
import os

class SocketIoClient:
    def __init__(self):
        load_dotenv()
        self.instance = socketio.Client()
        self.instance.on("connect", self.on_connect)
        self.instance.on("disconnect", self.on_disconnect)
        self.instance.on("message", self.on_message)
    
    def connect(self):
        server_url = os.getenv("SOCKETIO_SERVER_URL", "http://localhost:3000")
        self.instance.connect(server_url)
        
    def on_connect(self):
        print("Connected to Socket.IO server")
    
    def on_disconnect(self):
        print("Disconnected from Socket.IO server")
    
    def on_message(self, data):
        print("Message received:", data)
        