from fastapi import FastAPI
from routers import aqi
from loguru import logger

app = FastAPI()
app.include_router(aqi.router)

@app.get('/')
async def check_health():
    logger.info("I am good.")
    return {"Status":"ok"}