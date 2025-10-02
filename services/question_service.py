def generate_sample_questions(topic: str):
    # Mock data for now (later you can use LLM/AI here)
    return [
        {
            "id": 1,
            "question": f"Write a SQL query related to {topic}",
            "answer": "SELECT * FROM STATION WHERE MOD(ID,2)=0;"
        }
    ]
