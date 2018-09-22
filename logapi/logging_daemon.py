from pyloges.logger import Logger
from pyloges.classes.config import Config
from pyloges.handlers.file import FileHandler

from api import files

logger = Logger(Config())
logger.config.add_handler(FileHandler(files.get_and_create_data_folder() + "daemon-latest.log"))


def info(msg):
    logger.i(msg)


def debug(msg):
    logger.d(msg)


def warning(msg):
    logger.w(msg)


def error(msg):
    logger.e(msg)


def critical(msg):
    logger.f(msg)