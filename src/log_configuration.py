import logging
import pathlib
from logging.handlers import RotatingFileHandler

class LogConfiguration:
    def __init__(self, logger_name: str, log_file: str, log_format: str) -> None:
        self.logger_name = logger_name
        self.log_file = log_file
        self.log_format = log_format
     
    # TODO: Add a method to get the log file path using pathlib.Path.    
    @classmethod    
    def get_log_path(self) -> str:
        log_file = '~\\telemetry-ninja\\logs\\log.log'
        return log_file
        
    @staticmethod
    def enable(logger_name: str, log_file: str, log_format: str) -> tuple[object, str, object]:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(log_file, maxBytes=1e6, backupCount=5)
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger, log_file, log_format
    
    @staticmethod
    def disable():
        pass
        
    