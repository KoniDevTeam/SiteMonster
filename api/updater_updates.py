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
import threading
from logapi import logging_daemon as logging
from zipfile import ZipFile

import requests

import appinfo
from api import osinfo

VERSION_ID_FILE_ON_SERVER = '/SiteMonster/updater/version'
UPDATE_FILE_ON_SERVER = '/SiteMonster/latest.zip'
UPDATE_FILE = 'latest.zip'


def get_latest_version_id() -> int:
    """Get id of latest version from server."""

    logging.info("Getting latest updater version's id id from server")

    version_request = requests.get(appinfo.API_DOMAIN + VERSION_ID_FILE_ON_SERVER, timeout=3)

    if version_request.status_code != 200:
        logging.error("Can't get updater version, status code - " + str(version_request.status_code))
        raise ConnectionError("Can't updater app version, status code - " + str(version_request.status_code))

    return int(version_request.text)


def is_up_to_date() -> bool:
    """Check if newest version is installed."""

    if get_latest_version_id() == appinfo.UPDATER_VERSION_ID:
        logging.info('Updater is up to date!')
        return True
    else:
        logging.warning('Updater is not up to date!')
        return False


def download_new_version():
    """Download zip of latest version from server."""

    logging.info('Downloading new updater version binaries')

    update_file = open(UPDATE_FILE, 'wb')

    update_file.write(requests.get(appinfo.API_DOMAIN + UPDATE_FILE_ON_SERVER).content)

    update_file.close()


def remove_old_installation():
    """Remove old files."""

    logging.info('Removing old updater installation')

    if osinfo.is_win():
        os.remove('updater.exe')
    else:
        os.remove('updater')


def extract_new_version():
    """Extract files from archive."""

    logging.info('Unzipping new version')

    update_file = ZipFile(UPDATE_FILE, 'r')
    update_file.extractall('.')
    update_file.close()


def delete_update_archive():
    logging.debug('Removing update archive')
    os.remove(UPDATE_FILE)


class UpdaterUpdater(threading.Thread):
    """Downloads new version and installs it."""

    def run(self):
        """Begin updating."""

        logging.info("Update started")

        if is_up_to_date():
            logging.error('Already up to date')
            raise ValueError('Already up to date')

        download_new_version()

        remove_old_installation()

        extract_new_version()

        logging.info('Update finished')

        delete_update_archive()

        logging.info('Cleaned, exiting from thread')
