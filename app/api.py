from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["root"])
async def health_check() -> dict:
    return {"message": "Healthy boi"}
