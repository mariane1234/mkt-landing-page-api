# models.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.mysql import TINYTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)

class LeadProfiling(Base):
    __tablename__ = "lead_profiling"

    id = Column(Integer, primary_key=True, autoincrement=True) 
    leadId = Column(Integer, nullable=False) 
    source = Column(String(255), nullable=False)  
    target = Column(String(255), nullable=False)  
    business = Column(String(255), nullable=False)  
    businessDescription = Column(TINYTEXT, nullable=False)  

