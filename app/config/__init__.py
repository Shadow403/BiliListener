import platform


__version__ = "0.1.9-b1"
__platform__ = platform.system().lower()


from .logo import *
from .utils import *
from .config import *
