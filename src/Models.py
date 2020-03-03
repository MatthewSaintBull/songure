# pylint: disable=no-self-argument
from pydantic import BaseModel, ValidationError, validator
import re


class Error(BaseModel):
    message: str


class User(BaseModel):
    username: str
    full_name: str
    password: str
    email: str

    @validator('username')
    def username_is_valid(cls, v):
        if ' ' in v.title() or len(v.title()) > 16:
            raise ValueError('entered a non valide username')
        return v.title()

    @validator('full_name')
    def full_name_is_valid(cls, v):
        if ' ' not in v.title() or len(v.title()) > 50:
            raise ValueError('entered a non valide username')
        return v.title()

    @validator('password')
    def password_is_valid(cls, v):
        if re.match(r'[A-Za-z0-9@_!#$%^&+=]{8,}', v.title()):
            return v.title()
        else:
            raise ValueError('entered a non valid password')

    @validator('email')
    def email_is_valid(cls, v):
        pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
        print(v)
        if not re.match(pattern, v):
            raise ValueError('entered a non valid email')
        return v.title()
