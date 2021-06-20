from fastapi import FastAPI, HTTPException

from app.model import PostSchema

app = FastAPI()


@app.get("/", tags=["root"])
async def health_check() -> dict:
    return {"message": "Healthy boi"}


posts = [{"id": 1, "title": "Testing", "content": "Lorem Ipsum ..."}]

users = []


@app.get("/posts", tags=["posts"])
async def get_posts() -> dict:
    return {"data": posts}


@app.get("/posts/{id}", tags=["posts"])
async def get_single_posts(id: int) -> dict:
    for post in posts:
        if post["id"] == id:
            return {"data": post}

    raise HTTPException(status_code=404, detail="Post cannot be found")

@app.post("/posts", tags=["posts"])
async def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())

    return {
        "data": post
    }