from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Float, String
Base = declarative_base()

class Journey(Base):
    __tablename__ = "journeys"
    id = Column(Integer, primary_key=True, index=True)
    departure_station_id=Column(Integer, ForeignKey('stations.id'))
    return_station_id=Column(Integer, ForeignKey('stations.id'))
    departure_date = Column(DateTime)
    return_date = Column(DateTime)
    distance = Column(Float)
    duration = Column(Float)

class Station(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    city = Column(String, default="Helsinki", nullable=False)
    capacity = Column(Integer)
    x = Column(Float)
    y = Column(Float)