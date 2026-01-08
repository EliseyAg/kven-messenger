from flask_login import UserMixin

from RabbitMQ.RabbitMQ_Manager import RabbitMQManager


class UserLogin(UserMixin):
    def fromDB(self, user_id):
        RabbitMQManager.publish("user_ids_requests", str(user_id))
        self.__user = None
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user['id'])
