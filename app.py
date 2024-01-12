from fastapi import FastAPI
from logger import logger 
import uvicorn
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
#logger.info('Starting API...')

@app.get("/")
async def index() -> dict:
    #logger.info('Request to index page')
    return {'message': 'Hello'}

@app.get("/upload-videos")
async def upload_videos() -> dict:
    #logger.info('Request to video-upload page')
    return {'message': 'Video Uploaded'}

# uvicorn app:app --reload
# http://127.0.0.1:8000/docs#/

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)