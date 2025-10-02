from fastapi import APIRouter, HTTPException
from models.question_model import UserQuery
from api.question import questions_db

router = APIRouter()

@router.post("/{topic}/{qid}")
def validate_answer(topic: str, qid: int, user: UserQuery):
    qlist = questions_db.get(topic, [])
    for q in qlist:
        if q["id"] == qid:
            correct = q["answer"].strip().lower()
            user_ans = user.query.strip().lower()
            if correct == user_ans:
                return {"result": "Correct ✅"}
            else:
                return {"result": "Incorrect ❌", "expected": q["answer"]}
    raise HTTPException(status_code=404, detail="Question not found")
