import logging
import os


def setup_logger(logger_name='evony', level=logging.INFO):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s [%(name)s] [%(levelname)s] - %(message)s')

    # Get the parent directory of the current file (where this code is located)
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_file_dir)

    # Create the 'var' directory if it doesn't exist
    log_file = os.path.join(parent_dir, 'var', 'debug.log')
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create a file handler and a stream (console) handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Add the handlers to the root logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)