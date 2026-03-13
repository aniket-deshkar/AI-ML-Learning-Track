class ScraperException(Exception):
    """Exception raised for errors related to scraping errors."""
    pass

class FileOperationError(ScraperException):
    """Exception raised for errors related to file operations."""
    pass
