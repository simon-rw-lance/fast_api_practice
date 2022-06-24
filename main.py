from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/user/{user_id}")
async def user_profile(user_id: str):
    return {"user" : user_id}

@app.get('/blogs')
async def blogs(request: Request):
    return templates.TemplateResponse("blogs/index.html", {"request": request})
