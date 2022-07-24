from pathlib import Path

import uvicorn # type: ignore
from fastapi import APIRouter, FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.responses import Response

from config import HOST, PORT # type: ignore
from api import api_router # type: ignore

app: FastAPI = FastAPI()
page_router: APIRouter = APIRouter()

BASE_PATH: Path = Path(__file__).resolve().parent

TEMPLATES_DIR_NAME: str = "templates"
TEMPLATES: Jinja2Templates = Jinja2Templates(directory=str(BASE_PATH / TEMPLATES_DIR_NAME))

STATIC_DIR_NAME: str = "static"
app.mount("/" + STATIC_DIR_NAME, StaticFiles(directory=STATIC_DIR_NAME), name=STATIC_DIR_NAME)

ROUTERS: tuple = (page_router, api_router)


HOME_PAGE_TEMPLATE = "home_page/index.html"

@page_router.get("/", response_class=HTMLResponse)
async def homepage(request: Request) -> Response: # Jinja returns an inner type, wtf?
    """Starting page for the engine"""
    return TEMPLATES.TemplateResponse(
        HOME_PAGE_TEMPLATE,
        {"request": request},
    )


def main() -> None:
    """Main function"""
    for router in ROUTERS:
        app.include_router(router)
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
