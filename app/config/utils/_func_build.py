from .. import __version__

def get_type():
    if "b" in __version__:
        return "experimental"
    else:
        return "release"
