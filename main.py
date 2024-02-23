from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"my message": "Hello World!! is here"}


@app.get('/posts')
def get_posts():
    return {'data': ['my post1', 'my post 2', 'my post 3']}

@app.post('/createpost')
def create_post(payload: dict = Body(...)):
    print(payload)
    print(type(payload))
    return {'message': 'post created'}