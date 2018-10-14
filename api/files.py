"""Work with user's filesystem."""

# Copyright (C) 2018 Koni Dev Team, All Rights Reserved
# https://github.com/KoniDevTeam/SiteMonster/
#
# This file is part of Site Monster.
#
# Site Monster is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Site Monster is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Site Monster.  If not, see <https://www.gnu.org/licenses/>.

import os
import json
import platform
import sys

from api.osinfo import is_win, is_linux, is_mac_os

PATH = 'Koni Dev Team/Site Monster/'


def get_data_folder_windows() -> str:
    """ Returns data folder on windows.

    For example: `C://Users/Nikita/AppData/Roaming/Koni Dev Team/Site Monster/`.

    """

    path = os.getenv('APPDATA') + '/' + PATH
    return path


def get_data_folder_macos() -> str:
    """ Returns data folder on macOS.

    For example: `/User/nikita/Library/Preferences/Koni Dev Team/Site Monster/`.

    """

    path = os.getenv('HOME') + '/Library/Preferences/' + PATH
    return path


def get_data_folder_linux() -> str:
    """ Returns data folder on Linux.

    For example: `/home/nikita/.Koni Dev Team/Site Monster/`.

    """

    path = os.getenv('HOME') + '/.' + PATH
    return path


def get_and_create_data_folder() -> str:
    """Gets data folder.

    For more information see docs for  functions `get_data_folder_windows`,
    `get_data_folder_macos` and `get_data_folder_linux`.

    """

    folder = None

    if is_win():
        folder =  get_data_folder_windows()
    elif is_linux():
        folder = get_data_folder_linux()
    elif is_mac_os():
        folder = get_data_folder_macos()
    else:
        raise OSError("Unknown OS: " + platform.system())

    if not os.path.exists(folder):
        os.makedirs(folder)

    return folder


def save(obj: object, filename: str):
    """Make a json from obj and save to filename in data folder."""

    f = open(get_and_create_data_folder() + filename, "w")
    f.write(json.dumps(obj))
    f.close()


def read(filename: str):
    """Gets json from filename and loads it to dictionary/list."""

    f = open(get_and_create_data_folder() + filename, "r")

    obj = json.loads(f.read())

    f.close()

    return obj


def get_media_folder_path():
    """Return abs path for '..' folder, or for '.' in exe"""

    if hasattr(sys, 'frozen'):
        return os.path.abspath(os.path.dirname(sys.executable) + '/media')
    elif __file__:
        return os.path.abspath(os.path.dirname(__file__) + '/../media')
