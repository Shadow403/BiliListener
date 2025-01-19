import platform


__version__ = "0.2.1"
__platform__ = platform.system().lower()


from .logo import *
from .utils import *
from .config import *
