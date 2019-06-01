from flask import request
from flask_socketio import Namespace, emit
class room(Namespace):
    def on_connect(self):
        print(request.sid+" Joined")

    def on_disconnect(self):
        print(request.sid+" Left")

    def on_my_event(self, data):
        emit('my_response', data)