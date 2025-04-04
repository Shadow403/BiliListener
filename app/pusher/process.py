import sys
import time
import multiprocessing
from blivedm.log import logger

from .app import server
from .utils.tasks import *

def initAll():
    start_webserver()
    time.sleep(1)
    start_tasks()

def start_webserver():
    run_server = multiprocessing.Process(target=server)
    run_server.start()

def start_tasks():
    live_status_initializer()
    live_clear = multiprocessing.Process(target=live_clear_loop)
    live_status = multiprocessing.Process(target=live_status_loop)

    live_clear.start()
    live_status.start()

    live_clear.join()
    live_status.join()

def signal_handler(sig, frame):
    logger.info("Signal Interrupt Stop Process...")
    for p in multiprocessing.active_children():
        p.terminate()
        p.join(timeout=5)
        if p.is_alive():
            logger.warning(f"Process {p.name} did not terminate, forcing kill")
            p.kill()
    time.sleep(3)
    sys.exit(0)
