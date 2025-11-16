from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.models.user import User

router = APIRouter()


@router.get("/users", tags=["Users"])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT * FROM users")
    return {"users": [dict(row._mapping) for row in result]}
