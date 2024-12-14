import uvicorn

from pusher.app import app
from config import WebAPI, ASCII
from config.utils import init_config
from database.connector import config_database_init


def main():
    print(ASCII.pusher)
    config_database_init()
    init_config()

    uvicorn.run(app, host=WebAPI.HOST, port=WebAPI.PORT)

if __name__ == "__main__":
    main()
