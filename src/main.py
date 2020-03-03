from fastapi import FastAPI, HTTPException
from Models import User, Error
from starlette.responses import JSONResponse
from db import DB
import users

app = FastAPI()
db = DB()

# Registration
def check_existing_user(username: str):
    for user in users.users:
        if user["username"] == username:
            return True
    return False

@app.post("/register")
def register(user: User):
    if not db.register(user):
        raise HTTPException(
        status_code= 403,
        detail="User/Mail already exists"
    )
    return {
        'message':'User registered successfully'
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
