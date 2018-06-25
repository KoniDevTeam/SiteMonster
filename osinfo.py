import platform


def is_win10():
    return is_win() and '10' in platform.release()


def is_win():
    return 'Windows' in platform.system()


def is_mac_os():
    return 'Darwin' in platform.system()


def is_linux():
    return 'Linux' in platform.system()
