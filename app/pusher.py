import uvicorn
from pusher.app import app
from config import WebAPI, ASCII

def main():
    print(ASCII.pusher)
    uvicorn.run(app, host=WebAPI.HOST, port=WebAPI.PORT)

if __name__ == "__main__":
    main()
