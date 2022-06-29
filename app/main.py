from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    data = {
        "name": "Simon R. W. Lance",
        "email": "simon.rw.lance@gmail.com",
        "github": "https://github.com/simon-rw-lance"
    }
    return templates.TemplateResponse("contact.html", {"request": request, "data": data})

@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = {
        "page": page_name
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@app.get("/phd/{page_name}", response_class=HTMLResponse)
async def phd(request : Request, page_name: str):
    if page_name == "about":
        return templates.TemplateResponse("phd/about.html", {"request": request})
    elif page_name == "convection":
        return templates.TemplateResponse("phd/convection.html", {"request": request})
    elif page_name == "planets":
        return templates.TemplateResponse("phd/planets.html", {"request": request})

from app.routers import wow_tools
app.include_router(wow_tools.router)
