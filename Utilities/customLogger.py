import logging
import os
from logging.handlers import RotatingFileHandler


class LogGen:
    @staticmethod
    def loggen():
        log_directory = ".\\Logs\\"
        log_file = "automation.log"
        log_path = os.path.join(log_directory, log_file)

        # Check if log file exists, then delete it
        if os.path.exists(log_path):
            os.remove(log_path)

        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        logging.basicConfig(filename=log_directory + log_file,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %H:%M:%S', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        if logger.hasHandlers():
            logger.handlers.clear()
        # Add the rotating file handler to the logger
        return logger



