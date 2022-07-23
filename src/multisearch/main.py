from pathlib import Path

import uvicorn
from fastapi import APIRouter, FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
api_router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES_DIR_NAME = "templates"
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / TEMPLATES_DIR_NAME))

app.mount("/static", StaticFiles(directory="static"), name="static")

@api_router.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return TEMPLATES.TemplateResponse(
        "home_page/index.html",
        {"request": request},
    )


def main():
    app.include_router(api_router)
    uvicorn.run(app, host="localhost", port=8001)


if __name__ == "__main__":
    main()
