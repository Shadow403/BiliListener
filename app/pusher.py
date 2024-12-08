import os
import uvicorn
from pusher.app import app
from config import WebAPI, PathConfig, ASCII

def main():
    print(ASCII.pusher)

    if not os.path.exists(PathConfig.DATA_Path):
        os.makedirs(PathConfig.DATA_Path)

    uvicorn.run(app, host=WebAPI.HOST, port=WebAPI.PORT)

if __name__ == "__main__":
    main()
