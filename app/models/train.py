from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Train(Base):
    __tablename__ = "trains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    train_number = Column(String, unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)
