import asyncio
import random
import time

sem = asyncio.Semaphore(3)  # Concurrency Limit


# Scrape Function
async def scrape(url):
    async with sem:
        print(f"Start {url} at {time.strftime('%X')}")
        await asyncio.sleep(random.randint(1, 3))

        if random.choice([True, False]):
            raise ValueError(f"Failed {url}")

        print(f"END {url} at {time.strftime('%X')}")
        return f"Content from {url}"


# Main function
async def main():
    urls = [f"url_{i}" for i in range(1, 11)]
    tasks = [scrape(url) for url in urls]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    success = []
    failed = []

    for url, result in zip(urls, results):
        if isinstance(result, Exception):
            failed.append(url)
        else:
            success.append(result)

    print("\nSuccessful Results: ")
    for s in success:
        print(s)

    print("\nFiled Results: ")
    for f in failed:
        print(f)


asyncio.run(main())