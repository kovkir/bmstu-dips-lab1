from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from config.database import Base


class PersonModel(Base):
    __tablename__ = "persons"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    age = Column(Integer)
    address = Column(String)
    work = Column(String)
