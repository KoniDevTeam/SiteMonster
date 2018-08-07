"""Work with user's filesystem."""

import os
import json
import logging
import platform

from api.osinfo import is_win, is_linux, is_mac_os

PATH = 'Koni Dev Team/Site Monster/'


def get_data_folder_windows() -> str:
    """ Returns data folder on windows.

    For example: `C://Users/Nikita/AppData/Roaming/Koni Dev Team/Site Monster/`.

    """

    path = os.getenv('APPDATA') + '/' + PATH
    logging.debug("Got windows folder: " + path)
    return path


def get_data_folder_macos() -> str:
    """ Returns data folder on macOS.

    For example: `/User/nikita/Library/Preferences/Koni Dev Team/Site Monster/`.

    """

    path = os.getenv('HOME') + '/Library/Preferences/' + PATH
    logging.debug("Got macOS folder: " + path)
    return path


def get_data_folder_linux() -> str:
    """ Returns data folder on Linux.

    For example: `/home/nikita/.Koni Dev Team/Site Monster/`.

    """

    path = os.getenv('HOME') + '/.' + PATH
    logging.debug("Got linux folder: " + path)
    return path


def get_data_folder() -> str:
    """Gets data folder.

    For more information see docs for  functions `get_data_folder_windows`,
    `get_data_folder_macos` and `get_data_folder_linux`.

    """

    logging.debug("Getting user's data folder")

    if is_win():
        return get_data_folder_windows()
    elif is_linux():
        return get_data_folder_linux()
    elif is_mac_os():
        return get_data_folder_macos()
    else:
        raise OSError("Unknown OS: " + platform.system())


def save(obj: object, filename: str):
    """Make a json from obj and save to filename in data folder."""

    logging.debug("Saving " + str(obj) + ' to ' + filename)

    f = open(get_data_folder() + filename, "w")
    f.write(json.dumps(obj))
    f.close()


def read(filename: str):
    """Gets json from filename and loads it to dictionary/list."""

    logging.debug('Reading object from ' + filename)

    f = open(get_data_folder() + filename, "r")

    obj = json.loads(f.read())

    f.close()

    return obj
