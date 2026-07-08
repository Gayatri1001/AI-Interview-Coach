from pydantic import BaseModel

class Candidate(BaseModel):
    name: str
    email: str
    experience: int
    skills: list[str]
    