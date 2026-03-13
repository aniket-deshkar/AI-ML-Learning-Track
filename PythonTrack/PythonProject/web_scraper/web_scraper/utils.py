import logging
import functools
import asyncio

file_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/PythonProject/web_scraper/web_scraper/"
max_retries = 3

'''Defining Retry utility decorator where the max retry count is set to 3'''
#Retry decorator
def retry_utility(max_retries):
    def decorator(func):
        async def wrapper(*args,**kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    print("Attempt number :", attempt)
                    return await func(*args, **kwargs)
                except Exception as e:
                    print("Error:", e)
                    if attempt == max_retries:
                        logger.error(f"All attempts failed for {func.__name__}")
                        raise e
                    await asyncio.sleep(1)
            return None

        return wrapper
    return decorator

'''Defining logger configuration setup'''
def logger_config():
    logger = logging.getLogger("web_scraper")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handling = logging.FileHandler("web_scraper.log")
        file_handling.setFormatter(formatter)
        logger.addHandler(file_handling)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    return logger

logger = logger_config()

"""Defining log utility decorator function which can be used as decorator"""
def log_utility(func):
    '''Single wrapper that handles both sync and asnync'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Starting function: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            if asyncio.iscoroutine(result):
                async def await_result():
                    try:
                        return await result
                    except Exception as e:
                            logger.error(f"Error in {func.__name__} : {e}")
                            raise e
                return await_result()
            logger.info(f"Ending program {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__} : {e}")
            raise e
    return wrapper


