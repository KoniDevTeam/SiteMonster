"""Get some info about user's OS."""

import platform
import logging

from api import files


def init_log(sess_name):
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.DEBUG)
    logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                        level=logging.DEBUG, filename=files.get_data_folder() + 'latest-' + sess_name + '.log')


def log_pc_info():
    logging.info("Machine - " + platform.machine())
    logging.info("System - " + platform.system())
    logging.info("System release - " + platform.release())
    logging.info("System version - " + platform.version())
    logging.info("CPU - " + platform.processor())
    logging.info("uname - " + str(platform.uname()))


def is_win10() -> bool:
    is_win_10 = is_win() and '10' in platform.release()
    logging.debug("Checking for windows 10 -" + str(is_win_10))

    return is_win_10


def is_win() -> bool:
    is_win_ = 'Windows' in platform.system()
    logging.debug("Checking for windows -" + str(is_win_))

    return is_win_


def is_mac_os() -> bool:
    is_mac = 'Darwin' in platform.system()
    logging.debug("Checking for macOS -" + str(is_mac))

    return is_mac


def is_linux() -> bool:
    is_linux_ = 'Linux' in platform.system()
    logging.debug("Checking for linux -" + str(is_linux_))

    return is_linux_
