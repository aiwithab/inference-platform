from fastapi import FastAPI
from src.core.config import settings
from src.api.v1.routes.health import router as health_router
from src.api.v1.routes.users import router as users_router


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
    app.include_router(health_router, prefix=settings.API_V1_STR)
    return app


app = create_app()

app.include_router(users_router, prefix=settings.API_V1_STR)
