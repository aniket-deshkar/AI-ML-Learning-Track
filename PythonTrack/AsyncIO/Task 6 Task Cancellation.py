import asyncio


# --------Funtion for running delay -----#
async def long_run():
    # raising error for cancelling task after 3 sec
    try:
        print("Task Started...")
        for i in range(10):
            print(f"Running... {i + 1}s")
            await asyncio.sleep(1)

    except asyncio.CancelledError:
        print("Task was cancelled gracefully!")
        raise



async def main():
    task = asyncio.create_task(long_run())

    await asyncio.sleep(3)
    print("Cancelling task....")
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Main confirmed task cancellation")


asyncio.run(main())