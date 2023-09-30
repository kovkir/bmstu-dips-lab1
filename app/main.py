import uvicorn
from fastapi import FastAPI

from routers.api import router as api_router
from config.database import create_tables
from config.config import get_db_settings


create_tables()


app = FastAPI()
app.include_router(api_router, prefix="/api/v1")


if __name__ == '__main__':
    db_settings = get_db_settings()
    uvicorn.run(
        "main:app", 
        host=db_settings["POSTGRES_HOST"], 
        port=db_settings["POSTGRES_PORT"], 
        log_level="info",
        reload=True
    )
