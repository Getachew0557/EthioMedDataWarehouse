# src/logger_setup.py
import logging
import os

# Create logs directory if it doesn't exist
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'info.log'), mode='a'),
        logging.FileHandler(os.path.join(log_dir, 'error.log'), mode='a'),
        logging.StreamHandler()  # Print logs to console as well
    ]
)

# Create specific loggers for different log levels
info_logger = logging.getLogger('info_logger')
info_logger.setLevel(logging.INFO)

error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)
