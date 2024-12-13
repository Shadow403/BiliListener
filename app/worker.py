import sys

from config import ASCII
from worker.app import worker_initializer


def main():
    print(ASCII.worker)

    args = sys.argv
    if len(args) != 4:
        sys.exit()

    live_uid = args[1]
    live_room_id = args[2]
    live_timestamp = args[3]

    worker_initializer(live_uid, live_room_id, live_timestamp)

if __name__ == "__main__":
    main()
