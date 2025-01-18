import sys
from scripts import *


if __name__ == "__main__":
    args = sys.argv

    if args[0] == "-1":
        build_pusher()
    elif args[0] == "-2":
        build_worker()
    else:
        build_pusher()
        build_worker()
