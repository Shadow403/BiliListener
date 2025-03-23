import os

from config import __version__, __platform__, get_type

__ico_path__ = "./scripts/ico/"

ex = get_type()

def build_main():
    _build_ico = f"-i {__ico_path__}listener.ico"
    _bulid_name_ = f"-n pusher-{__platform__}-{__version__}-{ex}"
    os.system(f"pyinstaller {_build_ico} --onefile pusher.py {_bulid_name_} --clean")
