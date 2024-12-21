import os
import sys
import yaml

from ..logo import ASCII_LOGO


def init_config():
    data = {
        "api": {
            "host": "127.0.0.1",
            "port": 5000
        },
        "query_delay": 30,
        "data": {
            "path": "data"
        },
        "auth": {
            "sessdata": ""
        },
        "debug": False
    }

    config_path = "config.yml"

    if not os.path.exists(config_path):
        with open(config_path, "w") as f:
            yaml.dump(data, f, default_flow_style=False)
        print(ASCII_LOGO.pusher)
        print("config.yml 文件已生成, 请填写SESSDATA\n")
        os.system("pause")
        sys.exit(0)
