
# prueba de conexión
    
from fastapi import Request
from fastapi.responses import StreamingResponse

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

"""
@app.route("/")
async def index(request: Request):
    return JSONResponse(context.data)
"""

@app.get("/")
async def hello():
    """patient = Patient("nombre", "apellido", "dni", "44565456", "456", False)"""
    return {"message": "Hello, World!"}

@app.get("/info")
async def hello():
    return {"message": "Hello, World!"}

@app.get("/apiv2/info")
async def hellov2():
    return {"message": "Hello, World from V2"}