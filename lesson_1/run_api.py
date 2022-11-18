import uvicorn

from app.api.webapp import app


if __name__ == "__main__":
    # Используется исключительно для отладки.
    uvicorn.run(app)
