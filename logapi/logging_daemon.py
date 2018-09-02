from sclogger import Logger, MessageType

from api import files

logger = Logger(files.get_and_create_data_folder() + "/daemon.log")


def info(msg):
    logger.message(msg, MessageType.INFO)


def debug(msg):
    info(msg)


def warning(msg):
    logger.message(msg, MessageType.WARNING)


def error(msg):
    logger.message(msg, MessageType.ERROR)
    

def critical(msg):
    logger.message(msg, MessageType.ERROR)
