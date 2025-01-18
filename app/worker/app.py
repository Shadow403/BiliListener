import json
import asyncio

from config.utils import b64_decode

from .init import worker_db_initializer
from .worker import started_listening_initializer


def worker_initializer(data):
    live_config = eval(b64_decode(data))
    uid, rid, uuid, revert_data = worker_db_initializer(live_config)
    asyncio.run(started_listening_initializer(uid, rid, uuid, revert_data))
