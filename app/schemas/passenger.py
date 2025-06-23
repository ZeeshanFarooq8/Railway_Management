from pydantic import BaseModel

class PassengerBase(BaseModel):
    name: str
    age: int

class PassengerCreate(PassengerBase):
    pass

class PassengerOut(PassengerBase):
    id: int

    class Config:
        orm_mode = True
