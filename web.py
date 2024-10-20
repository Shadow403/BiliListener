import uvicorn
from web import app
from config import WebAPI

if __name__ == "__main__":
    uvicorn.run(app, host=WebAPI.HOST, port=WebAPI.PORT)
