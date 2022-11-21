import httpx
import asyncio

async def main(url):
    async with httpx.AsyncClient(proxies="") as client:
        for i in range(65535):
            if i % 100 == 0:
                print(f"reached port {i}")
            try:
                req = await client.get(f"{url}:{i}") 
                if req.status_code == 200:
                    print(f"{req.url} WORKS!")
            except: 
                pass

asyncio.run(main("http://0.0.0.0"))#change address
