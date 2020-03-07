from fastapi import APIRouter

from app.api.routes import register, login


router = APIRouter()
router.include_router(login.router, tags=["login"], )
router.include_router(register.router, tags=["register"], prefix="/api")
