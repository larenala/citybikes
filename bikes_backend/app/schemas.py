from pydantic import BaseModel
from datetime import datetime

class Station(BaseModel):
    id: int
    name: str
    address: str
    city: str
    x: int
    y: int 

class Journey(BaseModel):
    id: int
    departure_station_id: int
    return_station_id: int
    departure_date: datetime
    return_date: datetime
    distance: int
    duration: int
    class Config:
        orm_mode = True