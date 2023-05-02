import os
import csv
import time
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.db import engine, get_db

app = FastAPI()

DATA_DIRECTORY = '/data'

origins = [
    "http://localhost:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

INITIAL_DATA = { "stations": [], "journeys": [] }

def get_data():
    with open(f'{DATA_DIRECTORY}/Helsinki_and_Espoo_city_bike_stations.csv') as csv_file:
        reader = csv.reader(csv_file , delimiter=',', quotechar='"', skipinitialspace=True)
        headers = next(csv_file) 
        for line in reader:
            station = { "id": line[1], "name": line[2], "address": line[5], "city": line[7] if line[7] else "Helsinki", "capacity": line[10], "x": line[11], "y": line[12]}
            INITIAL_DATA["stations"].append(station)
    for file in os.listdir(f'{DATA_DIRECTORY}/journeys'):
        count = 0
        with open(f"{DATA_DIRECTORY}/journeys/{file}", newline="") as csv_file:
            reader = csv.reader(csv_file , delimiter=',', quotechar='"', skipinitialspace=True)
            headers = next(csv_file)
            for row in reader:
                if (count < 100):
                    # Ignore distances smaller than 10m as well as durations of less than 10s
                    if not row[6]  or float(row[6]) < 10.0 or float(row[7]) < 10.0:
                        continue
                    journey = { "departure_date": row[0], "return_date": row[1], "departure_station_id": row[2], "return_station_id": row[4], "distance": row[6], "duration": row[7] }
                    INITIAL_DATA["journeys"].append(journey)
                    count = count + 1

def initialize_table(target, connection, **kw):
    try:
        tablename = str(target)
        if tablename in INITIAL_DATA and len(INITIAL_DATA[tablename]) > 0:
            connection.execute(target.insert(), INITIAL_DATA[tablename])
    except:
        time.sleep(1)
        print(error)

event.listen(models.Station.__table__, 'after_create', initialize_table)
event.listen(models.Journey.__table__, 'after_create', initialize_table)

# This will create the DB schema and trigger the "after_create" event
@app.on_event("startup")
def configure():
    get_data()
    models.Base.metadata.create_all(bind=engine)

@app.get("/journeys")
async def list_all_journeys(db: Session = Depends(get_db)):
    return crud.list_all_journeys(db=db)

@app.get("/stations")
async def list_all_stations(db: Session = Depends(get_db)):
    return crud.list_all_stations(db=db)

