"""Work with user's filesystem."""

import os
import json

from api.osinfo import *

PATH = 'Koni Dev Team/Site Monster/'


def save(obj, filename):
    """Make a json from obj and save to filename in data folder."""

    f = open(get_data_folder() + filename, "w")
    f.write(json.dumps(obj))


def read(filename):
    """Gets json from filename and loads it to dictionary/list."""
    f = open(get_data_folder() + filename, "r")
    return json.loads(f.read())


def get_data_folder() -> str:
    """Gets data folder.

    For more information see docs for  functions `get_data_folder_windows`,
    `get_data_folder_macos` and `get_data_folder_linux`.

    """
    if is_win():
        return get_data_folder_windows()
    elif is_linux():
        return get_data_folder_linux()
    elif is_mac_os():
        return get_data_folder_macos()
    else:
        raise OSError("Unknown OS: " + platform.system())


def get_data_folder_windows() -> str:
    """ Returns data folder on windows.

    For example: `C://Users/Nikita/AppData/Roaming/Koni Dev Team/Site Monster/`.

    """
    return os.getenv('APPDATA') + '/' + PATH


def get_data_folder_macos() -> str:
    """ Returns data folder on macOS.

    For example: `/User/nikita/Library/Preferences/Koni Dev Team/Site Monster/`.

    """
    return os.getenv('HOME') + '/Library/Preferences/' + PATH


def get_data_folder_linux() -> str:
    """ Returns data folder on Linux.

    For example: `/home/nikita/.Koni Dev Team/Site Monster/`.

    """
    return os.getenv('HOME') + '/.' + PATH
