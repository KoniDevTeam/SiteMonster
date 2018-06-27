import os
import json

from api.osinfo import *

PATH = 'Koni Dev Team/Site Monster/'


def save(obj, filename):
    f = open(get_data_folder() + filename, "w")
    f.write(json.dumps(obj))


def read(filename):
    f = open(get_data_folder() + filename, "r")
    return json.loads(f.read())


def get_data_folder():
    if is_win():
        return get_data_folder_windows()
    elif is_linux():
        return get_data_folder_linux()
    elif is_mac_os():
        return get_data_folder_macos()
    else:
        raise OSError("Unknown OS: " + platform.system())


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
