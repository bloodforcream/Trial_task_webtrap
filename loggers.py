import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('[%(funcName)s:%(lineno)d]: %(levelname)s %(asctime)s: %(message)s',
                              "%Y-%m-%d %H:%M:%S")

logger_file_handler = RotatingFileHandler('logs.log', maxBytes=1024 * 1024, backupCount=5)
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

logger_stream_handler = logging.StreamHandler()
logger_stream_handler.setFormatter(formatter)
logger.addHandler(logger_stream_handler)
