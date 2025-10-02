# from fastapi import APIRouter

# list_of_topics = []
# router = APIRouter()

# @router.post("")
# async def add_topic(topic:str):
#     list_of_topics.append(topic)
#     return {"message":f"Topic {topic} added successfully in list"}

# @router.get("")
# async def topic_list():
#     return {"message":list_of_topics}


from fastapi import APIRouter
from models.topics_model import Topic

router = APIRouter()
topics = []

@router.post("/")
def add_topic(topic: Topic):
    topics.append(topic.topic)
    return {"message": "Topic added", "topics": topics}

@router.get("/")
def get_topics():
    return {"topics": topics}
