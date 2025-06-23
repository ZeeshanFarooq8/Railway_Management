from pydantic import BaseModel

class StationBase(BaseModel):
    name: str
    location: str

class StationCreate(StationBase):
    pass

class StationOut(StationBase):
    id: int

    class Config:
        from_attributes = True
