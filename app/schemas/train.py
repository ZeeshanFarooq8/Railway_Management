from pydantic import BaseModel

class TrainBase(BaseModel):
    name: str
    train_number: str
    capacity: int

class TrainCreate(TrainBase):
    pass

class TrainOut(TrainBase):
    id: int

    class Config:
        from_attributes = True
