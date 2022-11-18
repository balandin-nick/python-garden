from typing import Any, Dict

from fastapi import FastAPI

from app.settings.db import service_database_settings


app = FastAPI(
    title="Lesson 2",
    description="Test FastApi application for Python Garden",
)


@app.get("/")
def hello_world() -> Dict[str, Any]:
    return {"settings": service_database_settings.dict()}
