import yaml
from ._func_init_config import init_config

def read_config():
    init_config()

    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)
    
    return config
