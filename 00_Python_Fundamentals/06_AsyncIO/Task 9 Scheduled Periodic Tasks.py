import asyncio


async def periodic_task(interval,n):
    for i in range(n):
        print(f"tick {i + 1}")
        await asyncio.sleep(interval)

async def other_task():
    print("Starting other task")
    await asyncio.sleep(5)
    print("Finished other task")

async def main():
    await asyncio.gather(periodic_task(1,5),other_task())

asyncio.run(main())