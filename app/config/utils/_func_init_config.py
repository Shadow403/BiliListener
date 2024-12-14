import os
import sys
import yaml

from ..config import PathConfig

def init_config():
    data = {
        "auth": {
            "sessdata": ""
        }
    }
    config_path = PathConfig.CONF_Path

    if not os.path.exists(config_path):
        with open(config_path, "w") as f:
            yaml.dump(data, f, default_flow_style=False)
        print("config.yml 文件已生成, 请填写SESSDATA\n")
        os.system("pause")
        sys.exit(0)
