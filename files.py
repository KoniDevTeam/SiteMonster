import json
import platform
import os

PATH = 'Koni Dev Team/Site Monster/'
SITES_LIST_FILE = 'siteList.json'
USER_DATA_FILES = 'userData.json'

BLANK_SITE_LIST = {"sites": []}


def get_site_list():
    if os.path.exists(get_data_folder() + SITES_LIST_FILE):
        file = open(get_data_folder() + SITES_LIST_FILE, 'r')
        return json.loads(file)
    else:
        return BLANK_SITE_LIST


def save_site_list_obj(json_obj):
    file = open(get_data_folder() + SITES_LIST_FILE, 'w')
    file.write(json.dumps(json_obj))


def get_user_data():
    file = open(get_data_folder() + USER_DATA_FILES, 'r')
    return json.loads(file)


def save_user_data(json_obj):
    file = open(get_data_folder() + USER_DATA_FILES, 'w')
    file.write(json.dumps(json_obj))


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
