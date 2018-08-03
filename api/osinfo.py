"""Get some info about user's OS."""

import platform
import logging

from api import files


def init_log():
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.DEBUG)
    logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                        level=logging.DEBUG, filename=files.get_data_folder() + 'latest.log')


def log_pc_info():
    logging.info("Machine - " + platform.machine())
    logging.info("System - " + platform.system())
    logging.info("System release - " + platform.release())
    logging.info("System version - " + platform.version())
    logging.info("CPU - " + platform.processor())
    logging.info("uname - " + str(platform.uname()))


def is_win10() -> bool:
    return is_win() and '10' in platform.release()


def is_win() -> bool:
    return 'Windows' in platform.system()


def is_mac_os() -> bool:
    return 'Darwin' in platform.system()


def is_linux() -> bool:
    return 'Linux' in platform.system()
