from pymongo import MongoClient
from Models import User
from config import config

class DB():
    def __init__(self, env: str = "dev"):
        if env == "dev":
            self.client = MongoClient(config.config["dev"]["db_host"], authSource='songure')
            self.db = self.client[config.config["dev"]["db_name"]]
        print("DB CONNECTED @ ENV:",env)

    def register(self, user: User):
        if not self.search_user(user):
            self.db["users"].insert_one(user.dict())
            return True
        return False

    def search_user(self, user: User):
        #Check if user already exists in db
        pass
