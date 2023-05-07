from pydantic import BaseModel, validator
from datetime import datetime

class Station(BaseModel):
    id: int
    name: str
    address: str
    city: str
    x: int
    y: int 

    class Config:
        orm_mode = True

class Journey(BaseModel):
    id: int
    departure_station_id: int
    return_station_id: int
    departure_date: datetime
    return_date: datetime
    distance: int
    duration: int

    
    @validator('distance')
    def distance_must_be_over_10m(cls, value):
        if value < 10:
            raise ValueError('Journey distance must be over 10 meters.')
        return v

    @validator('duration')
    def duration_must_be_over_10s(cls, value):
        if value < 10:
            raise ValueError('Journey duration must over 10 seconds.')
        return value

    class Config:
        orm_mode = True