from pydantic import Field, SecretStr

from .base import BASE_DIRECTORY, AdvancedBaseSettings


class ServiceDatabaseSettings(AdvancedBaseSettings):
    """
    Этим именем мы явно даём понять, что данная база является для сервиса основной.

    В конфигурации данного класса мы дополнительно указываем префикс service_db,
    при помощи которого визуально объединяем эти энвы в группу.

    Префикс присоединяется спереди к имени атрибута,
    после чего ищет в списке соответствующую переменную:
        - service_db_host;
        - service_db_username;
        - service_db_name;
        - service_db_port;
    """
    host: str
    username: str
    password: SecretStr  # Пароль будет искать в файле (см. ниже)
    db_name: str = Field(..., env="service_db_name")  # Если не указать имя явно, то будет искать service_db_db_name
    port: int = Field(default="5432")

    class Config:
        env_prefix = "service_db_"
        secrets_dir = BASE_DIRECTORY / "secrets"  # директория, где хранится файл с паролем.

    @property
    def postgresql_url(self) -> str:
        """
        Запомни, падаван: строки легче конкатенировать, чем парсить!
        Это property (свойство) пригодится нам в будущем, когда будем подключаться к БД.
        """
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"


service_database_settings = ServiceDatabaseSettings()
