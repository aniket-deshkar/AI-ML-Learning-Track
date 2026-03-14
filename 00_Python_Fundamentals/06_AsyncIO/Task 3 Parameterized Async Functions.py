import asyncio


async def fetch_data(url):
    await asyncio.sleep(1)
    return f"Data from {url}"
async def main():
    urls = ["https://www.python.org/", "https://www.google.com/"]
    results = await asyncio.gather(*(fetch_data(url)for url in urls))
    print(results)

asyncio.run(main())