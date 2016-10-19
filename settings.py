import sys
import logging


def set_logger():
    console_handle = logging.StreamHandler(sys.stdout)
    logger = logging.getLogger()
    logger.addHandler(console_handle)
    logger.setLevel(logging.DEBUG)

    return logger