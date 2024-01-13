from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware
import asyncio
import requests

app = FastAPI(
    title="Patient Middleware App",
    description="System meant for recording, timing and documentation of endpoints. It manages the information of a basic crud patient application.",
    port=8003
    )
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

@app.get("/pacientes")
async def get_patients() -> dict:
    try:
        response = requests.get(' http://127.0.0.1:5000/pacientes')
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return JSONResponse(response.json())

    except requests.exceptions.ConnectionError as err:
        raise HTTPException(
            status_code=503, detail="Failed to connect to upstream server. Please try again later."
        ) from err

    except requests.exceptions.RequestException as err:
        raise HTTPException(
            status_code=500, detail="An error occurred while processing the request."
        ) from err

@app.get("/")
async def index() -> dict:
    return {'message': 'Hello'}

@app.get("/upload-videos")
async def upload_videos() -> dict:
    await asyncio.sleep(1.5)
    return {'message': 'Video Uploaded'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)