import asyncio
import random


async def fetch_data(url):
    delay = random.randint(1, 3)
    await asyncio.sleep(delay)
    # Random Failure
    if random.choice([True, False]):
        raise ValueError(f"Error Fetching {url}")
    return f"Success from {url}"


# -------Concurrent Function-------#
async def main():
    urls = [f"url_{i}" for i in range(1, 6)]

    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    success = []
    failed = []

    for url, result in zip(urls, results):
        if isinstance(result, Exception):
            failed.append((url, str(result)))
        else:
            success.append((url, result))

    print("\nSuccessful Results: ")
    for s in success:
        print(s)

    print("\nFiled Results: ")
    for f in failed:
        print(f)


asyncio.run(main())