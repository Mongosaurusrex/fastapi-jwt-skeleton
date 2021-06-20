from fastapi import FastAPI, HTTPException, Body, Depends

from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

app = FastAPI()


@app.get("/", tags=["root"])
async def health_check() -> dict:
    return {"message": "Healthy boi"}


posts = [{"id": 1, "title": "Testing", "content": "Lorem Ipsum ..."}]

users = []


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.get("/posts", tags=["posts"])
async def get_posts() -> dict:
    return {"data": posts}


@app.get("/posts/{id}", tags=["posts"])
async def get_single_posts(id: int) -> dict:
    for post in posts:
        if post["id"] == id:
            return {"data": post}

    raise HTTPException(status_code=404, detail="Post cannot be found")


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())

    return {"data": post}


@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(
        user
    )  # replace with db call, making sure to hash the password first with for instance bcrypt or passlib
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)

    raise HTTPException(status_code=401, detail="Email or password is wrong")
