from pydantic import BaseModel
from sqlalchemy import true

""" class ApiResponse(BaseModel) :
  message: str
  data: any """

class IPatient(BaseModel):
    name: str
    surname: str
    typeOfDocument: str
    documentNumber: str
    medicalHistoryNumber: str
    enabled: true