from pathlib import Path

from pydantic import BaseSettings


BASE_DIRECTORY = Path(__file__).absolute().parent.parent.parent


class AdvancedBaseSettings(BaseSettings):
    # Родительский объект с общими настройками.
    # Нужен для того, чтобы не описывать несколько раз одно и то же.

    class Config:
        allow_mutation = False  # Эта настройка делает объект неизменяемым.
