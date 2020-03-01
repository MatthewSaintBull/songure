from pydantic import BaseModel


class Error(BaseModel):
    message: str 

class User(BaseModel):
    username: str
    full_name: str = None
    password: str
    email: str
