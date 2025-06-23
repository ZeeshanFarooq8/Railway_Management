

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.train_route import TrainRoute
from app.schemas.train_route import TrainRouteCreate, TrainRouteOut

router = APIRouter()

@router.post("/routes", response_model=TrainRouteOut)
def create_route(route: TrainRouteCreate, db: Session = Depends(get_db)):
    db_route = TrainRoute(**route.dict())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route

@router.get("/routes", response_model=list[TrainRouteOut])
def get_routes(db: Session = Depends(get_db)):
    return db.query(TrainRoute).all()

@router.get("/routes/{route_id}", response_model=TrainRouteOut)
def get_route(route_id: int, db: Session = Depends(get_db)):
    route = db.query(TrainRoute).get(route_id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    return route

@router.delete("/routes/{route_id}")
def delete_route(route_id: int, db: Session = Depends(get_db)):
    route = db.query(TrainRoute).get(route_id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    db.delete(route)
    db.commit()
    return {"msg": "Route deleted successfully"}
