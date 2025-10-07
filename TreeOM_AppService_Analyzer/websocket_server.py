import asyncio
import websockets

connected = set()

async def handler(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            for conn in connected:
                if conn != websocket:
                    await conn.send(f"Broadcast: {message}")
    finally:
        connected.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 6789):
        await asyncio.Future()  # run forever

asyncio.run(main())
