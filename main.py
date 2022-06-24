from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
async def home():
    return {"message": "Hello World"}

@app.get("/user/{user_id}")
async def user_profile(user_id: str):
    return {"user" : user_id}
