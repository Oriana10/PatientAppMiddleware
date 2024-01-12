from fastapi import FastAPI
from logger import logger 
import uvicorn
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware
import asyncio

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

@app.get("/")
async def index() -> dict:
    return {'message': 'Hello'}

@app.get("/upload-videos")
async def upload_videos() -> dict:
    await asyncio.sleep(1.5)
    return {'message': 'Video Uploaded'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)