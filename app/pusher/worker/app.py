import asyncio

from .init import worker_db_initializer
from .worker import started_listening_initializer


def worker_initializer(data):
    live_config = worker_db_initializer(data)
    try:
        asyncio.run(started_listening_initializer(live_config))
    except KeyboardInterrupt:
        pass
