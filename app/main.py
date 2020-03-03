
from app.api.routes.api import router as api_router
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

from app.core.events import create_start_app_handler


def get_application() -> FastAPI:

    application = FastAPI(title="Songure")
    application.include_router(api_router)

    application.add_event_handler("startup", create_start_app_handler(application))

    return application


app = get_application()

