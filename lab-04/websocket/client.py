import tornado.ioloop
import tornado.websocket
import asyncio

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    async def connect_and_read(self):
        print("Connecting...")
        try:
            self.connection = await tornado.websocket.websocket_connect(
                url="ws://localhost:8888/websocket/",
                ping_interval=10,
                ping_timeout=30
            )
            await self.read_messages()
        except Exception as e:
            print(f"Could not connect: {e}, retrying in 3 seconds...")
            self.io_loop.call_later(3, lambda: asyncio.ensure_future(self.connect_and_read()))

    async def read_messages(self):
        while True:
            try:
                message = await self.connection.read_message()
                if message is None:
                    print("Disconnected from server, reconnecting...")
                    await self.connect_and_read()
                    break
                print(f"Received word from server: {message}")
            except Exception as e:
                print(f"Error while reading message: {e}")
                await self.connect_and_read()
                break

def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    io_loop.add_callback(lambda: asyncio.ensure_future(client.connect_and_read()))
    io_loop.start()

if __name__ == "__main__":
    main()
