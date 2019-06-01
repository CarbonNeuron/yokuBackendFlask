import socketio

sio = socketio.Client()

@sio.on("connect")
def connect():
    print("I'm connected!")

@sio.on("my response")
def handler(data):
    print(data)


sio.connect('http://localhost:5000',namespaces=['/chat'])

