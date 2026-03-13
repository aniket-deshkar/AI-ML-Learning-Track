import asyncio
import time


async def fetch(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def parse(data):
    await asyncio.sleep(0.5)
    return f"Parsed Data: {data}"

async def store(parsed_data):
    await asyncio.sleep(0.5)
    return f"Stored Data: {parsed_data}"

async def run_pipeline(url):
    try:
        d = await fetch(url)
        p = await parse(d)
        s = await store(p)
        return s
    except Exception as e:
        print(e)

async def main():
    start = time.perf_counter()
    urls = ["https://www.python.org/", "https://www.google.com/", "https://www.youtube.com/"]
    tasks = [asyncio.create_task(run_pipeline(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)
    end = time.perf_counter()
    print(f"Total time: {end - start}")

asyncio.run(main())