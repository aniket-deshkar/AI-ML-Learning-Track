import  asyncio
import time

async def say_hello(name):
    print(f"Hello {name}")
    await asyncio.sleep(1)

def run():
    start = time.perf_counter()
    asyncio.run(say_hello("Aniket"))
    end = time.perf_counter()
    print(f"Elapsed time: {end - start}")
run()