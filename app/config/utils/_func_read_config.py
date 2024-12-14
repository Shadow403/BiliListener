import yaml
from ..config import PathConfig


def read_config(
        sessdata: bool = True
    ):
    with open(PathConfig.CONF_Path, "r") as f:
        load_config = yaml.safe_load(f)
    
    if sessdata:
        load_config = load_config["auth"]["sessdata"]

    return load_config
