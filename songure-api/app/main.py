
from app.api.api import router as api_router
from fastapi import FastAPI
from starlette.exceptions import HTTPException


def get_application() -> FastAPI:
    import os 
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    application = FastAPI(title="Songure")
    application.include_router(api_router)
    return application


app = get_application()

