import asyncio
from .init import worker_db_initializer
from .worker import started_listening_initializer

def worker_initializer(live_uid, live_room_id, live_timestamp):
    revert_data, uuid = worker_db_initializer(live_uid, live_timestamp)
    asyncio.run(started_listening_initializer(live_uid, uuid, live_room_id, revert_data))
