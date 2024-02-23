from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional[int] = 23

@app.get("/")
def root():
    return {"my message": "Hello World!! is here"}


@app.get('/posts')
def get_posts():
    return {'data': ['my post1', 'my post 2', 'my post 3']}

@app.post('/my_route')
def create_post(new_post: Post):
    print(new_post, type(new_post))
    print(new_post.model_dump())
    return new_post.model_dump()
    # return {'data': 'new post'}
