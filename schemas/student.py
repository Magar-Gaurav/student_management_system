from pydantic import Field, BaseModel, ConfigDict
from typing import Optional

class StudentCreate(BaseModel):
    name : str = Field(..., min_length = 3, max_length = 100)
    age : int = Field(...,gt = 0, le = 99)
    rank : int = Field(...,gt = 0, le = 50)
    email : str

class StudentUpdate(BaseModel):
    name : Optional[str] = Field(default = None, min_length = 3, max_length = 100)
    age : Optional[int] = Field(default = None, gt = 0, le = 99)
    rank : Optional[int] = Field(default = None, gt = 0, le = 50)
    email : Optional[str] = None

class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes = True)

    id : int
    name : str
    age : int
    rank : int
    email : str