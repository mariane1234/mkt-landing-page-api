from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from src.database import get_db, engine
from src.models import Base, Lead, LeadProfiling
from src.schemas import LeadSchema, LeadProfilingSchema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.post("/leads/")
def create_lead(leadData: LeadSchema, db: Session = Depends(get_db)):
    newLead = Lead(name=leadData.name, email=leadData.email)
    db.add(newLead)
    db.commit()
    db.refresh(newLead)
    return newLead


@app.post("/leads/profiling")
def create_lead(leadProfData: LeadProfilingSchema, db: Session = Depends(get_db)):
    newLeadProfiling = LeadProfiling(leadId=leadProfData.leadId, 
                            source=leadProfData.source, 
                            target=leadProfData.target,
                            business=leadProfData.business,
                            businessDescription=leadProfData.businessDescription)
    db.add(newLeadProfiling)
    db.commit()
    db.refresh(newLeadProfiling)
    return newLeadProfiling


@app.get("/leads/")
def get_leads(db: Session = Depends(get_db)):
    leads = db.query(Lead).all()
    return leads


@app.get("/")
async def root():
    return {"message": "Hello World"}