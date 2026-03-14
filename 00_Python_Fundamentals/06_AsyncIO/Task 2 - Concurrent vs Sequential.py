import asyncio
import time


async def task1():
    await asyncio.sleep(2)
    print("T1")



async def task2():
    await asyncio.sleep(2)
    print("T2")


print("----Running Task1 Task2 using gather----")
async def run_async():
    s = time.perf_counter()
    print("Using Async gather")
    await asyncio.gather(task1(), task2())
    t = time.perf_counter() - s
    print(f"Async Time {t:.2f} seconds")


print("-----Running Task1 Task2 sequentially----")
async def run_seq():
    s = time.perf_counter()
    print("Using Seq function")
    await task1()
    await task2()
    t = time.perf_counter() - s
    print(f"Sequential time : {t:.2f} seconds")


asyncio.run(run_async())
asyncio.run(run_seq())