

from fastapi import APIRouter
from fastapi import FastAPI
from fastapi_injector import attach_injector
from injector import Injector
from simple_settings import settings

app = FastAPI()


@app.on_event("startup")
async def startup_app():
    main_router = APIRouter(prefix="/api/v1")
    injector = Injector()
    attach_injector(app, injector)

    for component_class in settings.COMPONENTS:
        component = component_class(
            application=app,
            injector=injector,
            parent_router=main_router,
        )
        await component.setup()

    app.include_router(main_router)
