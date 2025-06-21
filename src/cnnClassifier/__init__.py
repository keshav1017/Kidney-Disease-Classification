import logging
import sys
import pandas as pd
import numpy as np
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

# constants for log configurations
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024 # 5 MB
BACKUP_COUNT = 3 # Number of backup log files to keep

# Construct log file path
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)

# create a custom logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Define formatter
formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

# File handler with rotation
file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def error_message_details(error: Exception, error_details: sys) -> str:
    """
    Extracts detailed error information including file name, line number and the error message

    :param error: The exception that occured.
    :param error_details: The sys module to access traceback details.
    :returns: A formatted error message string.
    """
    # Extracts traceback details (exception information)
    _, _, exc_tb = error_details.exc_info()

    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message string with file name, line number and the actual error message
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in python script: [{file_name}] at line number [{line_number}]: {str(error)}"

    # log the error for better tracking
    logging.error(error_message)

    return error_message

class MyException(Exception):
    """
    Custom exception class for handling errors in the US visa application.
    """
    def __init__(self, error_message: str, error_detail: sys):
        """
        Initializes the USvisaException with a detailed error message.

        :param error_message: A string describing the error.
        :param error_detail: The sys module to access traceback error.
        """
        # call the base class constructor with the error message
        super().__init__(error_message)

        # format the detailed error message using the error_message_detail function
        self.error_message = error_message_details(error_message, error_detail)
    
    def __str__(self):
        """
        Returns the string representation of the error message.
        """
        return self.error_message