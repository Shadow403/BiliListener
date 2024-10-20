import asyncio
from .worker import main
from ..database import init_data

def init_listen(uid, room_id):
    session = init_data(uid)
    asyncio.run(main(uid, room_id, session))
