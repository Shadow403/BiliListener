import sys
import time
import multiprocessing
from blivedm.log import logger

from .router import main as ws
from .app import http_server as http
from .utils.tasks import live_clear_loop, live_status_loop


def initAll():
    start_webserver()
    time.sleep(1)
    start_tasks()

def start_webserver():
    ws_p = multiprocessing.Process(target=ws)
    http_p = multiprocessing.Process(target=http)

    ws_p.start()
    http_p.start()

    # ws_p.join()
    # http_p.join()

def start_tasks():
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
    time.sleep(5)
    sys.exit(0)
