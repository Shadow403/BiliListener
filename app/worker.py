import sys
import ctypes

from config import ASCII_LOGO
from worker.app import worker_initializer


kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x00|0x100))

def main():
    print(ASCII_LOGO.worker)

    args = sys.argv
    if len(args) != 4:
        sys.exit()

    live_uid = args[1]
    live_room_id = args[2]
    live_timestamp = args[3]

    worker_initializer(live_uid, live_room_id, live_timestamp)

if __name__ == "__main__":
    main()
