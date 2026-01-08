from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, emit

from RabbitMQ.RabbitMQ_Manager import RabbitMQManager
from UserLogin import UserLogin


app = Flask(__name__, static_folder="static")
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Авторизуйтесь для доступа к закрытым страницам'
login_manager.login_message_category = 'success'


@login_manager.user_loader
def load_user(user_id):
    print("load user")
    return UserLogin().fromDB(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    if 'user_id' in session:
        user_login = UserLogin().create(session['user_id'])
        login_user(user_login)
        return
    else:
        return redirect(url_for('/login'))


@app.route('/messenger/')
def messenger():
    return render_template("messenger.html")


@app.route('/messenger/personlist')
def personlist():
    return render_template("personlist.html")


@app.route('/messenger/chat', methods=['POST', "GET"])
@login_required
def chat():
    print(current_user.username)
    return render_template("chat.html")


if __name__ == '__main__':
    RabbitMQManager.__init__("localhost", 5672)

    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
