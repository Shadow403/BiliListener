import ctypes
import signal
import multiprocessing
from colorama import init

from config import config, ASCII_LOGO
from pusher import initAll, signal_handler
from database.connector import config_database_init



init(autoreset=True)

if not config.debug:
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x00|0x100))


def main():
    print(ASCII_LOGO.pusher)
    config_database_init()
    initAll()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    signal.signal(signal.SIGINT, signal_handler)
    main()
