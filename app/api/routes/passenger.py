from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.passenger import PassengerCreate, PassengerOut
from app.services.passenger import create_passenger, get_all_passengers
from app.db.session import get_db

router = APIRouter(prefix="/passengers")

@router.post("/", response_model=PassengerOut)
def create(passenger: PassengerCreate, db: Session = Depends(get_db)):
    return create_passenger(db, passenger)

@router.get("/", response_model=list[PassengerOut])
def read_all(db: Session = Depends(get_db)):
    return get_all_passengers(db)
