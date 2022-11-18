# Lesson 1

Проект является обучающим материалом для [статьи](https://habr.com/ru/post/692952/).

Запускается через [poetry](https://python-poetry.org).

Однако если ты не знаком с данной технологией, то запускай любым удобным тебе способом. Например:

- создай виртуальное окружение: `python3 -m venv .pythonenv/`;
- активируй его: `source .pythonenv/bin/activate`;
- инсталлируй «змеиные» пакеты: `pip install -r requirements`;
- далее добавь нужные переменные окружения: `export SERVICE_DB_HOST="0.0.0.0"` 
(см. раздел «Список переменных окружения»);
- проделай действия из раздела «Обязательные действия перед запуском»;
- запусти один из раннеров (см. раздел «Точки входа»).


## Обязательные действия перед запуском

- создай в корне проекта папку `secrets`;
- внутри неё создай файл `event_broker_password` без расширения с любым текстом внутри (это пароль от кролика);
- создай файл `service_db_password` без расширения с любым текстом внутри (это пароль от БД).


## Точки входа

Проект имеет две точки входа:
- `run_api` — запуск апишки, по корневому URL которой (http://127.0.0.1:8000/) можно увидеть энвы БД;
- `run_consumer` — якобы запуск консьюмера, но на самом деле просто печать энвов БД и MQ.


## Список переменных окружения

### API

- `SERVICE_DB_HOST` (example: 0.0.0.0);
- `SERVICE_DB_NAME` (example: service_db);
- `SERVICE_DB_USERNAME` (example: db_user);
- `SERVICE_DB_PORT` (example: 5432, default: 5432).


### Consumer

- `SERVICE_DB_HOST` (example: 0.0.0.0);
- `SERVICE_DB_USERNAME` (example: db_user);
- `SERVICE_DB_NAME` (example: service_db);
- `SERVICE_DB_PORT` (example: 5432, default: 5432);
- `EVENT_BROKER_HOST` (example: 0.0.0.0);
- `EVENT_BROKER_USERNAME` (example: mq_user);
- `EVENT_BROKER_PORT` (example: 5672, default: 5672).
- `EVENT_BROKER_VHOST` (example: core, default: /);
