import socketio
from dotenv import load_dotenv
import os

class SocketIoClient:
    def __init__(self):
        load_dotenv()
        self.sio = socketio.Client()
        self.sio.on("connect", self.on_connect)
        self.sio.on("disconnect", self.on_disconnect)
        self.sio.on("message", self.on_message)
    
    def connect(self):
        server_url = os.getenv("SOCKETIO_SERVER_URL", "http://localhost:3000")
        self.sio.connect(server_url)
        
    def on_connect(self):
        print("Connected to Socket.IO server")
    
    def on_disconnect(self):
        print("Disconnected from Socket.IO server")
    
    def on_message(self, data):
        print("Message received:", data)
        