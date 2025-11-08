from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, current_user
from flask_socketio import SocketIO, emit

from RabbitMQ.RabbitMQ_Manager import RabbitMQManager


app = Flask(__name__, static_folder="static")
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route('/messenger')
def messenger():
    return render_template("messenger.html")


@app.route('/personlist')
def personlist():
    return render_template("personlist.html")


if __name__ == '__main__':
    RabbitMQManager.__init__("localhost", 5672)

    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
