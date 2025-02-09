from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.item import item_router
from app.routes.greeting import greeting_router

import uvicorn


def get_application() -> FastAPI:
    app = FastAPI(
        prefix="/api/v1",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(item_router)
    app.include_router(greeting_router)
    return app


app: FastAPI = get_application()


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
    )
