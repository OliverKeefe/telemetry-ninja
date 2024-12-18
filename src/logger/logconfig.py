import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler


class LogConfiguration:
    def __init__(self, logger_name: str, log_file: str, log_format: str) -> None:
        self.logger_name = logger_name
        self.log_file = log_file
        self.log_format = log_format

    def get_log_path() -> str:
        log_file = Path("..", "logs", "telemetry_ninja.log")
        log_file_path = str(log_file.expanduser().resolve())
        return log_file_path

    def enable(
        logger_name: str, log_file: str, log_format: str
    ) -> tuple[object, str, object]:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(log_file, maxBytes=1e6, backupCount=5)
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger, log_file, log_format

    def disable(logger) -> None:
        if logger:
            handlers = logger.handlers[:]
            for handler in handlers:
                handler.close()
                logger.removeHandler(handler)
            logger.info("Logging disabled")
