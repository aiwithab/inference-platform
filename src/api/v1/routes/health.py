from fastapi import APIRouter
from src.core.config import settings

router = APIRouter()


@router.get('/health', tags=["Health"])
def health_check():
    return {
        "status": "200 OK",
        "message": "Inference Platform API is healthy",
        "project": settings.PROJECT_NAME,
        "api_version": settings.API_V1_STR
    }
