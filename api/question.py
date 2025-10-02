from fastapi import APIRouter
from models.question_model import Question
from services import question_service

router = APIRouter()
questions_db = {}

@router.post("/{topic}")
def generate_questions(topic: str):
    sample_questions = question_service.generate_sample_questions(topic)
    questions_db[topic] = sample_questions
    return sample_questions
