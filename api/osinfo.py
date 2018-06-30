"""Get some info about user's OS."""

import platform


def is_win10() -> bool:

    return is_win() and '10' in platform.release()


def is_win() -> bool:
    return 'Windows' in platform.system()


def is_mac_os() -> bool:
    return 'Darwin' in platform.system()


def is_linux() -> bool:
    return 'Linux' in platform.system()
