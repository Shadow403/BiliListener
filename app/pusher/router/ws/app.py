import threading
from colorama import Fore, Style
from websockets.sync.server import serve

from config import config
from .hub import ws_hub


def register(websocket):
    message_thread = threading.Thread(target=ws_hub, args=(websocket,))
    message_thread.daemon = True
    message_thread.start()

    try:
        # SOCKET GET
        for message in websocket:
            if config.debug:
                print(f"{Fore.WHITE}INFO{Style.RESET_ALL}:     WebSocket: {message} GET")
    except Exception as e:
        if config.debug:
            print(f"{Fore.YELLOW}WARNING{Style.RESET_ALL}:    WebSocket: {e}")

def main():
    print(f"{Fore.GREEN}INFO{Style.RESET_ALL}:     Starting websocket process")
    print(f"{Fore.GREEN}INFO{Style.RESET_ALL}:     Websocket ready on ws://{config.host}:{config.ws_port}")
    with serve(register, config.host, config.ws_port) as server:
        server.serve_forever()

if __name__ == "__main__":
    main()
