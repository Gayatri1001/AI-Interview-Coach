from fastapi import APIRouter,status
from app.schemas.interview import Candidate


router = APIRouter()

@router.get("/")
def home():
    return {
        "message" :  "Welcome to AI Interview Coach"
    }

@router.get("/")
def about():
    return {
        "project": "AI Interview Coach",
        "framework": "FastAPI"
    }

@router.get("/users/{user_id}")
def get_user(user_id:int):
    return{
        "user_id" : user_id
    }

@router.get("/search")
def search(skill:str, experience:int):
    return{
        "skill" : skill,
        "experience": experience
    }

@router.post("/candidate",
    status_code=status.HTTP_201_CREATED)
def create_candidate(candidate:Candidate):
    return{
        "message": "Candidate added successfully",
        "candidate": candidate
    }
