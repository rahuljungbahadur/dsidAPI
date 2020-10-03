from typing import List, Optional, Dict
from pydantic import BaseModel

class results(BaseModel):
    name : str
    label : float
    min : Optional[str] = None
    class Config:
        orm_mode = True

class defaultResults(BaseModel):
    product : int
    name : str
    min : float
    max : float
    label : float
    meanEstimate : float
    meanStdError : float

    class Config:
        orm_mode = True