import asyncio
import random
import time



async def fetch_data(api_name):
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    return f"Data from {api_name} after {delay}s"


apis = [f"API={i}" for i in range(1, 6)]



async def concurrent_fetch(apis):
    tasks = [fetch_data(api) for api in apis]
    result = await asyncio.gather(*tasks)

    print("\nConcurrent Results:")
    for res in result:
        print(res)



async def sequential_fetch(apis):
    print("\n Sequential Result: ")
    for api in apis:
        result = await fetch_data(api)
        print(result)


# --------Running Both-----#
async def main(apis):
    s1 = time.perf_counter()
    print("---Cocurrent Fetch---")
    await concurrent_fetch(apis)
    e1 = time.perf_counter() - s1
    print(f"\n Time taken by Concurrent Fetch is: {e1:.2f} seconds")

    s = time.perf_counter()
    print("\n---Sequential Fetch---")
    await sequential_fetch(apis)
    e = time.perf_counter() - s
    print(f"\n Time taken by Sequential Fetch is: {e:.2f} seconds")


asyncio.run(main(apis))