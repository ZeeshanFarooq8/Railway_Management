from pydantic import BaseModel

class TrainRouteBase(BaseModel):
    route_name: str
    source_station_id: int
    destination_station_id: int

class TrainRouteCreate(TrainRouteBase):
    pass

class TrainRouteOut(TrainRouteBase):
    id: int

    class Config:
        from_attributes = True
