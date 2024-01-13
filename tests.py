
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



    """ try:
        response = requests.get('http://127.0.0.1:8000/pacientes')
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return JSONResponse(response.json())

    except requests.exceptions.ConnectionError as err:
        raise HTTPException(
            status_code=503, detail="Failed to connect to upstream server. Please try again later."
        ) from err

    except requests.exceptions.RequestException as err:
        raise HTTPException(
            status_code=500, detail="An error occurred while processing the request."
        ) from err """

""" @app.get("/patient")
async def get_patients():
    response = requests.get('http://localhost:4000') 
    return JSONResponse(response.json()) """
    
""" @app.post("/patient")
async def get_patients(request: IPatient):
    # print("aa ", request.data)    
    #return JSONResponse(request.data)
    return {'message': 'Patient'} """
    
    
################
@app.get("/pacientes")
async def get_patients() -> dict:
    return {'message': 'Patient'} 

@app.get("/")
async def index() -> dict:
    try:
        response = requests.get('http://127.0.0.1:8000/pacientes')
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
    # return {'message': 'Hello'}