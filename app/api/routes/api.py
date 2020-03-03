from fastapi import APIRouter

from app.api.routes import register


router = APIRouter()
router.include_router(register.router, tags=["register"], prefix="/v1")