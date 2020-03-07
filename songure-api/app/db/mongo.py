# pylint: disable=no-name-in-module
from pymongo import MongoClient
from app.models.user import User, OauthUser
from app.config.config import config
from app.db.singleton import Singleton


class DB(metaclass=Singleton):
    def __init__(self, env: str = "dev"):
        if env == "dev":
            self.uri = "mongodb://{username}:{password}@{host}:{port}".format(
                username=config["dev"]["db_admin"], password=config["dev"]["db_password"],
                host=config["dev"]["db_host"], port=config["dev"]["db_port"],
            )
            self.client = MongoClient(self.uri)
            self.db = self.client[config["dev"]["db_name"]]
        print("DB CONNECTED @ ENV:", env)

    def register(self, user: dict):
        if not self.search_user(user):
            self.db["users"].insert_one(user)
            return True
        return False

    def search_user_by_email(self, email):
        result = self.db["users"].find_one({"email": email})
        if result:
            return True
        return False

    def search_user_by_username(self, username):
        result = self.db["users"].find_one({"username": username})
        if result:
            return True
        return False

    def search_user(self, user: dict):
        result = self.db["users"].find_one(
            {"$or": [{"username": user["username"]}, {"email": user["email"]}]})
        if result:
            return True
        return False
