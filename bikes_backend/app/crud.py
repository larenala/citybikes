from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false, null 

from app import models, schemas

def list_all_journeys(db: Session):
    return db.query(models.Journey).all()

def list_all_stations(db: Session):
    print('getting stations')
    return db.query(models.Station).all()
