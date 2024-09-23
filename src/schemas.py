from pydantic import BaseModel

class LeadSchema(BaseModel):
    name: str
    email: str
    
class LeadProfilingSchema(BaseModel):
    leadId: int
    source: str
    target: str
    business: str
    businessDescription: str

