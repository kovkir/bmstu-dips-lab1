import uvicorn
from fastapi import FastAPI

from routers.api import router as api_router
from config.database import create_tables


create_tables()


app = FastAPI()
app.include_router(api_router, prefix="/api/v1")


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8006, log_level="info", reload=True)
