# from fastapi import FastAPI
# from fastapi import APIRouter
# # from api.add_topic import add_topic, topic_list
# from api.add_topic import router as add_topic_router

# app = FastAPI(title="SQL Practice application using GenAi")



# app.include_router(add_topic_router, prefix="/topic", tags=["topic"])

# # router = APIRouter()



from fastapi import FastAPI
from api import topics, question, validate

app = FastAPI(title="SQL Practice App with AI")

# Register routers
app.include_router(topics.router, prefix="/topics", tags=["Topics"])
app.include_router(question.router, prefix="/questions", tags=["Questions"])
app.include_router(validate.router, prefix="/validate", tags=["Validation"])
