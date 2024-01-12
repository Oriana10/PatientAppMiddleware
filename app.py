import string
from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel
from sqlalchemy import true
import uvicorn

# uvicorn app:app --reload
# http://127.0.0.1:8000/docs#/

app = FastAPI()

# prueba de conexión

class IPatient(BaseModel):
    name: string
    surname: string
    typeOfDocument: string
    documentNumber: string
    medicalHistoryNumber: string
    enabled: true
    
@app.middleware("http")
async def modify_request_response_middleware(request: Request, call_next):
    # Intercept and modify the incoming request
    request.scope["path"] = str(request.url.path).replace("api", "apiv2")
    # Process the modified request
    response = await call_next(request)
    # Transform the outgoing response
    if isinstance(response, StreamingResponse):
        response.headers["X-Custom-Header"] = "Modified"
    return response

@app.post("/patient/")
async def create_patient(patient: IPatient):
    return patient

# logs

@app.get("/")
async def index() -> dict:
    return {'message': 'Hello'}

@app.get("/upload-videos")
async def upload_videos() -> dict:
    return {'message': 'Video Uploaded'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

