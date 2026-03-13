import logging


# Configure logging to write to 'app.log'
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,  
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
    filemode='a'  # 'a' for append (default), 'w' for write (overwrite)
)

logger = logging.getLogger("API Logger")


