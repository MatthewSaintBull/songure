from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.db.mongo import DB

db = DB()
router = APIRouter()

@router.get('/')
def index():
    return {
        "ok":"logged in"
    }