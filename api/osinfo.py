"""Get some info about user's OS."""

import platform
import logging


PID_FILE = 'daemon_pid.tmp'


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
