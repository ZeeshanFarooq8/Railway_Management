from fastapi import FastAPI
from app.api.routes.passenger import router as passenger_router
from app.db.base import Base
from sqlalchemy import create_engine
from app.core.config import settings  # ✅ Make sure this is here!

from app.api.routes.train import router as train_router
from app.api.routes.station import router as station_router
from app.api.routes.train_route import router as train_route_router
from app.api.routes.auth import router as auth_router





engine = create_engine(settings.DATABASE_URL)  # ✅ Use the correct name


def create_app() -> FastAPI:
    app = FastAPI(title="Railway Management System")

    # Create all tables
    Base.metadata.create_all(bind=engine)

    # Include API routes
    app.include_router(passenger_router, prefix="/api/v1", tags=["Passengers"])
    app.include_router(train_router, prefix="/api/v1", tags=["Trains"])
    app.include_router(station_router, prefix="/api/v1", tags=["Stations"])
    app.include_router(train_route_router, prefix="/api/v1", tags=["TrainRoutes"])
    app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
    return app

app = create_app()
