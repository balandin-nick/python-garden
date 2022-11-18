# Lesson 2

Проект является обучающим материалом для [статьи](https://habr.com/ru/post/694872/).

## Обязательные действия перед запуском

- создай в корне проекта папку `secrets`;
- внутри неё создай файл `event_broker_password` без расширения с паролем от кролика (`python_garden`);
- создай файл `service_db_password` без расширения с паролем от БД (`postgres`).

## Для владельцев Apple M1

Создай файл `docker-compose.override.yml`:

```yaml
version: "3.4"
services:
  service_db:
    platform: linux/arm64/v8
  mq:
    platform: linux/arm64/v8
```
