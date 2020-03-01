from fastapi import FastAPI, HTTPException
from Models import User, Error
from starlette.responses import JSONResponse

import users

app = FastAPI()


# Registration
def check_existing_user(username: str):
    for user in users.users:
        if user["username"] == username:
            return True
    return False

@app.post("/register")
def register(user: User):
    if check_existing_user(user.username):
        raise HTTPException(
            status_code=403,
            detail="Username already Exists"
        )
    else:

        return {
            'message': 'User registered successfully'
        }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
