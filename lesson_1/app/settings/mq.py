from pydantic import Field, SecretStr

from .base import BASE_DIRECTORY, AdvancedBaseSettings


class EventBrokerSettings(AdvancedBaseSettings):
    # Здесь имя говорит о наличии событий и некоем посреднике (брокере).
    # В данном случае любой мало-мальски опытный разработчик поймёт,
    # что речь идёт об инфраструктурном элементе, посредством которого
    # сервис получает на вход сообщения, инициирующие запуск тех или иных операций.
    host: str
    username: str
    password: SecretStr
    port: int = Field(default='5672')
    vhost: str = Field(default='/')

    class Config:
        env_prefix = "event_broker_"
        secrets_dir = BASE_DIRECTORY / "secrets"

    @property
    def amqp_url(self) -> str:
        return f'amqp://{self.username}:{self.password}@{self.host}:{self.port}/{self.vhost}'


event_broker_settings = EventBrokerSettings()
