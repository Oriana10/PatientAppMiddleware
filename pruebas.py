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