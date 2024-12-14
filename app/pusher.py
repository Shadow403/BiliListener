import uvicorn

from pusher.app import app
from config import config, ASCII_LOGO
from config.utils import init_config
from database.connector import config_database_init


def main():
    print(ASCII_LOGO.pusher)
    config_database_init()
    init_config()

    uvicorn.run(app, host=config.host, port=config.port)

if __name__ == "__main__":
    main()
