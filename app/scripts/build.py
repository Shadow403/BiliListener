import os

from config import __version__, __platform__

__ico_path__ = "./scripts/ico/"

def build_pusher():
    _build_ico = f"-i {__ico_path__}listener.ico"
    _bulid_name_ = f"-n pusher-{__platform__}-{__version__}"
    os.system(f"pyinstaller {_build_ico} --onefile pusher.py {_bulid_name_} --clean")

def build_worker():
    _build_ico_ = f"-i {__ico_path__}websocket.ico"
    _bulid_name_ = f"-n worker-{__platform__}-{__version__}"
    os.system(f"pyinstaller {_build_ico_} --onefile worker.py {_bulid_name_} --clean")

