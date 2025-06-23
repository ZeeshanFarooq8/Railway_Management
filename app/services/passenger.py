from sqlalchemy.orm import Session
from app.models.passenger import Passenger
from app.schemas.passenger import PassengerCreate

def create_passenger(db: Session, passenger: PassengerCreate):
    new_passenger = Passenger(**passenger.dict())
    db.add(new_passenger)
    db.commit()
    db.refresh(new_passenger)
    return new_passenger

def get_all_passengers(db: Session):
    return db.query(Passenger).all()
