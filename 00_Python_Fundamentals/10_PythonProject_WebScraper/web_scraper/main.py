import time
import asyncio

from web_scraper import ExtendedScraper

'''Defining the URLs to be called'''
urls= [
        "https://www.example.com",
       "https://www.google.com",
       "https://www.geeksforgeeks.org/",
       "https://stackoverflow.com/questions",
       "https://docs.python.org/3/",
       "https://www.browserstack.com/",
       "https://www.w3schools.com/",
       "https://bytebytego.com/",
       "https://medium.com/",
       "https://www.python.org/"

]

file_name = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/PythonProject/web_scraper/web_scraper/results.json"

'''Asynchronous main function declaration'''
async def main():
    scrapper = ExtendedScraper(limit=5)
    for url in urls:
        scrapper.add_urls(url)
    print("---Running sequentially---")
    seq_start_counter = time.perf_counter()
    await scrapper.run_sequential()
    print(f"Sequential call finished in {time.perf_counter() - seq_start_counter:.2f} seconds")

    '''Resets success and fail urls counter to 0 before making concurrent calls'''
    scrapper.reset()

    print("---Running concurrently---")
    concurrent_start_counter = time.perf_counter()
    await scrapper.run_all()
    print(f"Concurrent call finished in {time.perf_counter() - concurrent_start_counter:.2f} seconds")

    '''Saves the file'''
    scrapper.save_results(file_name)
    '''Loads the file'''
    scrapper.load_results(file_name)

'''Calling the main function'''
if __name__ == "__main__":
    asyncio.run(main())


