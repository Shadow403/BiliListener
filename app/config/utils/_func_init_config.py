import os
import sys
import yaml

from ..logo import ASCII_LOGO


def init_config():
    path = 'config.yml'

    data = {
        "api": {
            "host": "127.0.0.1",
            "port": 5700,
            "ws_port": 5701,
            "ws_push_delay": 5,
            "cors": ["10.20.0.1"],
            "router_access":{
                "strict": True,
                "r_put_uid": ["127.0.0.1"]
            }
        },
        "live_query_delay": 30,
        "live_clear_delay": 300,
        "data": {
            "root": "data",
            "db_path": "db",
            "json": {
                "enable": False,
                "json_path": "json"
            }
        },
        "auth": {
            "sessdata": ""
        },
        "debug": False,
        "hide_console": True
    }

    if not os.path.exists(path):
        with open(path, "w") as f:
            yaml.dump(data, f, default_flow_style=False)

        print(ASCII_LOGO.pusher)
        print(f"{path} 文件已生成, 请填写SESSDATA\n")
        os.system("pause")
        sys.exit(0)
