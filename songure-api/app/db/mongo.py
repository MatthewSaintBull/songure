# pylint: disable=no-name-in-module
from pymongo import MongoClient
from app.models.user import User
from app.config.config import config
from app.db.singleton import Singleton


class DB(metaclass=Singleton):
    def __init__(self, env: str = "dev"):
        if env == "dev":
            self.uri = "mongodb://{username}:{password}@{host}:{port}".format(
                    username = config["dev"]["db_admin"], password = config["dev"]["db_password"],
                    host = config["dev"]["db_host"], port = config["dev"]["db_port"],
                )
            self.client = MongoClient(self.uri)
            self.db = self.client[config["dev"]["db_name"]]
        print("DB CONNECTED @ ENV:", env)

    def register(self, user: User):
        if not self.search_user(user):
            self.db["users"].insert_one(user.dict())
            return True
        return False

    def search_user(self, user: User):
        if self.db["users"].find_one({"$or": [{"username": user.username}, {"email": user.email}]}):
            return True
