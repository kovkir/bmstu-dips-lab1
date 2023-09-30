import uvicorn
from fastapi import FastAPI

from routers.api import router as api_router
from config.database import create_tables
from config.config import get_db_settings


create_tables()


app = FastAPI()
app.include_router(api_router, prefix="/api/v1")


if __name__ == '__main__':
    settings = get_db_settings()
    uvicorn.run(
        "main:app", 
        host=settings["app"]["host"],
        port=settings["app"]["port"],
        log_level=settings["app"]["log_level"],
        reload=settings["app"]["reload"],
    )
