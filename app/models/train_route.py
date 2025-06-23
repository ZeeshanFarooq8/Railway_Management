from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class TrainRoute(Base):
    __tablename__ = "train_routes"

    id = Column(Integer, primary_key=True, index=True)
    route_name = Column(String, nullable=False, unique=True)
    source_station_id = Column(Integer, ForeignKey("stations.id"), nullable=False)
    destination_station_id = Column(Integer, ForeignKey("stations.id"), nullable=False)
