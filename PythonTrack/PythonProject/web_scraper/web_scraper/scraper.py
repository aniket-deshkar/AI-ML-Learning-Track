import json
import os.path
import httpx
import asyncio
import time

from bs4 import BeautifulSoup
from web_scraper.utils import retry_utility, max_retries, log_utility, logger
from .exceptions import  FileOperationError

#Headers are required in httpx.get() calls to provide necessary metadata to the server,
# ensuring requests are processed correctly, securely, and efficiently.
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"}

'''Defining Scraper class'''
class Scraper:
    '''__init__ constructor'''
    def __init__(self, limit= 3):
        self.urls= []
        self.results={}
        self.limit = limit
        self.success = 0
        self.failed = 0

    @retry_utility(max_retries)
    @log_utility
    async def fetch(self,client,url):
        try:
            response = await client.get(url, timeout=30)
            print("Status Code: ",response.status_code)
            response.raise_for_status()
            self.results[url] = response.text
            self.success += 1
            return response.text
        except Exception as e:
            self.failed += 1
            print(f"Success :{self.success} failed :{self.failed}")
            logger.error(f"Failed to fetch: {url} with exception: {e}")
            raise e


    """Function to add a new url, send a message if the url exists in the list"""
    def add_urls(self,url):
        if url not in self.urls:
            self.urls.append(url)
        else:
            print(f"Url {url} already exists")


    '''Resets success and failed counters'''
    def reset(self):
        self.success = 0
        self.failed = 0

    '''Saves results into a json file'''
    @log_utility
    def save_results(self,file_name):
        try:
            with open(file_name, 'w') as save_outfile:
                    json.dump(self.results, save_outfile, indent=4)
                    print(f"{file_name} was saved successfully")
        except FileOperationError as file_error:
            print(f"File write failed due to {file_error}")

    '''loads results from a json file'''
    @log_utility
    def load_results(self,file_name):
        if not os.path.exists(file_name):
            return
        try:
             with open(file_name, 'r') as load_infile:
                self.results = json.load(load_infile)
                logger.info(f"Loaded results from {file_name}")
        except FileOperationError as file_error:
            print(f"File read failed due to {file_error}")

    '''Asynchronous function to call GET requests sequentially'''
    async def run_sequential(self):
        async with httpx.AsyncClient(headers= headers, follow_redirects=True) as client:
            for url in self.urls:
                try:
                    await self.fetch(client, url)
                except Exception as e:
                    pass

    '''Calls all the methods in Scrapper Class'''
    @log_utility
    async def run_all(self):
        logger.info(f"Running all {len(self.urls)} urls")
        semaphore = asyncio.Semaphore(self.limit)
        #This function is defined for concurrent calls
        async def bounded_fetch(client, url):
            async with httpx.AsyncClient(headers=headers, follow_redirects=True) as client:
                async with semaphore:
                    try:
                        await self.fetch(client, url)
                    except Exception as e:
                        logger.error(f"Failed to fetch url in run_all: {url} with exception: {e}")
                
                tasks = [bounded_fetch(client, url) for url in self.urls]
                await asyncio.gather(*tasks, return_exceptions=True)

'''ExtendedScrapper which inherits the Scrapper class filters the HTML response and formats into desired json format'''
class ExtendedScraper(Scraper):
    async def fetch(self,client,url):
        html_content = await super().fetch(client,url)
        soup = BeautifulSoup(html_content, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"

        length = len(html_content)
        '''Output JSON structure'''
        data_object = {
            "url": url,
            "title": title,
            "length": str(length)
        }
        self.results[url] = data_object
        return html_content
