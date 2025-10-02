from pydantic import BaseModel

class Question(BaseModel):
    id: int
    question: str
    answer: str

class UserQuery(BaseModel):
    query: str
