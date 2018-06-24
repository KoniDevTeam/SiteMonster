import platform
import os

PATH = 'Koni Dev Team/Site Monster/'


def get_data_folder():
    sys = platform.system()
    if 'Windows' in sys:
        return get_data_folder_windows()
    elif 'Linux' in sys:
        return get_data_folder_linux()
    elif 'Darwin' in sys:
        return get_data_folder_macos()
    else:
        raise OSError("Unknown OS: " + sys)


def get_data_folder_windows():
    """ Returns data folder on windows. For example: C://Users/Nikita/AppData/Roaming/Koni Dev Team/Site Monster/

    """
    return os.getenv('APPDATA') + '/' + PATH


def get_data_folder_macos():
    """ Returns data folder on macOS. For example: /User/nikita/Library/Preferences/Koni Dev Team/Site Monster/'

    """
    return os.getenv('HOME') + '/Library/Preferences/' + PATH


def get_data_folder_linux():
    """ Returns data folder on Linux. For example: /home/nikita/.Koni Dev Team/Site Monster/'

    """
    return os.getenv('HOME') + '/.' + PATH
