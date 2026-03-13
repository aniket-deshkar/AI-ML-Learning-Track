import asyncio


async def fetch_data(url):
    return f"Data fro {url}"

async def process(data):
    return data.upper()

async def main():
    url = "http://httpbin.org/get"
    raw =await fetch_data(url)
    processed =await process(raw)
    print(processed)

asyncio.run(main())