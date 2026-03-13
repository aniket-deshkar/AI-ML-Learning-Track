import asyncio
import time


async def func1():
    print("Task 1 Started...")
    await asyncio.sleep(2)
    print("Task 1 Finished...")


async def func2():
    print("Task 2  Started...")
    await asyncio.sleep(1)
    print("Task 2 Finished...")


async def func3():
    print("Task 3 Started...")
    await asyncio.sleep(3)
    print("Task 3 Finished...")


async def main():
    s = time.perf_counter()

    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())
    task3 = asyncio.create_task(func3())

    await asyncio.gather(task1, task2, task3)
    e = time.perf_counter() - s
    print(f"Total time: {e:.2f} seconds")


asyncio.run(main())
