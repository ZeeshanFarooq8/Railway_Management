from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.train import Train
from app.schemas.train import TrainCreate, TrainOut

router = APIRouter()

@router.post("/trains", response_model=TrainOut)
def create_train(train: TrainCreate, db: Session = Depends(get_db)):
    db_train = Train(**train.dict())
    db.add(db_train)
    db.commit()
    db.refresh(db_train)
    return db_train

@router.get("/trains", response_model=list[TrainOut])
def get_trains(db: Session = Depends(get_db)):
    return db.query(Train).all()

@router.get("/trains/{train_id}", response_model=TrainOut)
def get_train(train_id: int, db: Session = Depends(get_db)):
    train = db.query(Train).get(train_id)
    if not train:
        raise HTTPException(status_code=404, detail="Train not found")
    return train

@router.delete("/trains/{train_id}")
def delete_train(train_id: int, db: Session = Depends(get_db)):
    train = db.query(Train).get(train_id)
    if not train:
        raise HTTPException(status_code=404, detail="Train not found")
    db.delete(train)
    db.commit()
    return {"msg": "Train deleted successfully"}
