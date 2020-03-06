from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.db.mongo import DB

db = DB()
router = APIRouter()

@router.post("/register")
def register(user: User):
    print(user)
    if not db.register(user.dict())[0]:
        raise HTTPException(
        status_code= 403,
        detail="User/Mail already exists"
    )
    return {
        'message':'User registered successfully'
    }