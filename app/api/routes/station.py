from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.station import Station
from app.schemas.station import StationCreate, StationOut
from app.logger import logger

router = APIRouter()

@router.post("/stations", response_model=StationOut)
def create_station(station: StationCreate, db: Session = Depends(get_db)):
    db_station = Station(**station.dict())
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station

@router.get("/stations", response_model=list[StationOut])
def get_stations(db: Session = Depends(get_db)):
    return db.query(Station).all()

@router.get("/stations/{station_id}", response_model=StationOut)
def get_station(station_id: int, db: Session = Depends(get_db)):
    station = db.query(Station).get(station_id)
    if not station:
        logger.info("Station not found.")
        raise HTTPException(status_code=404, detail="Station not found")
    return station

@router.delete("/stations/{station_id}")
def delete_station(station_id: int, db: Session = Depends(get_db)):
    station = db.query(Station).get(station_id)
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    db.delete(station)
    db.commit()


    logger.info("Station deleted successfully.")
    return {"msg": "Station deleted successfully"}
