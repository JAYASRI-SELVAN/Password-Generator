from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(_name_)
socketio = SocketIO(app)

active_users = set()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('send_message')
def handle_message(message):
    print('Message received:', message)
    emit('receive_message', message, broadcast=True)

if _name_ == '_main_':
    socketio.run(app)