from flask import Flask
from flask_socketio import SocketIO

app = Flask('N3U1R0N')
socketio = SocketIO(app)

from routes import *