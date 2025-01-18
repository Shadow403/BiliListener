import os
import sys
import ctypes

from config import ASCII_LOGO, config
from worker.app import worker_initializer

if not config.debug:
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x00|0x100))

def main():
    print(ASCII_LOGO.worker)

    args = sys.argv
    if len(args) != 2 and config.debug:
        print(args)
        os.system("pause")
        sys.exit()

    worker_initializer(args[1])

if __name__ == "__main__":
    main()
