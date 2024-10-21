import asyncio
from .worker import main
from ..database import init_data

def init_listen(uid, room_id, livetime):
    lost, session = init_data(uid, livetime)
    asyncio.run(main(uid, room_id, lost, livetime, session))
