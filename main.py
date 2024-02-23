from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"my message": "Hello World!! is here"}


@app.get('/posts')
def get_posts():
    return {'data': ['my post1', 'my post 2', 'my post 3']}