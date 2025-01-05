import ctypes
import uvicorn
from colorama import init

from pusher.app import app
from config import config, ASCII_LOGO
from database.connector import config_database_init


init(autoreset=True)

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x00|0x100))

def main():
    print(ASCII_LOGO.pusher)
    config_database_init()

    uvicorn.run(app, host=config.host, port=config.port)

if __name__ == "__main__":
    main()
