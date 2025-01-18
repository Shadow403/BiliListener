import platform


__version__ = "0.2.0"
__platform__ = platform.system().lower()

def get_type():
    if "b" in __version__:
        ex = "experiment"
    else:
        ex = "release"
    
    return ex

from .logo import *
from .utils import *
from .config import *
