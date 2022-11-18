from pprint import pprint

from app.settings.db import service_database_settings
from app.settings.mq import event_broker_settings


if __name__ == "__main__":
    pprint(event_broker_settings.dict(), indent=4)
    pprint(service_database_settings.dict(), indent=4)
