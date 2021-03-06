"""App update tool."""

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
import shutil
import threading
from logapi import logging_daemon as logging
from zipfile import ZipFile

import requests

import appinfo

VERSION_ID_FILE_ON_SERVER = '/SiteMonster/version'
VERSION_NAME_FILE_ON_SERVER = '/SiteMonster/version_name'
VERSION_CHANGELOG_FILE_ON_SERVER = '/SiteMonster/changelog'
UPDATE_FILE_ON_SERVER = '/SiteMonster/latest.zip'
UPDATE_FILE = 'latest.zip'
BACKUP_FOLDER = 'backup'


def get_latest_version_id() -> int:
    """Get id of latest version from server."""

    logging.info("Getting latest version's id id from server")

    version_request = requests.get(appinfo.API_DOMAIN + VERSION_ID_FILE_ON_SERVER, timeout=3)

    if version_request.status_code != 200:
        logging.error("Can't get app version, status code - " + str(version_request.status_code))
        raise ConnectionError("Can't get app version, status code - " + str(version_request.status_code))

    return int(version_request.text)


def get_latest_version_name() -> str:
    """Get name of latest version from server. (e.g. v1.0)"""

    logging.info("Getting latest version's name id from server")

    version_request = requests.get(appinfo.API_DOMAIN + VERSION_NAME_FILE_ON_SERVER)

    if version_request.status_code != 200:
        logging.error("Can't get app version name, status code - " + str(version_request.status_code))
        raise ConnectionError("Can't get app version name, status code - " + str(version_request.status_code))

    return version_request.text


def get_changelog() -> str:
    """Get changelog from server."""

    logging.info("Getting changelog from server")

    changelog_request = requests.get(appinfo.API_DOMAIN + VERSION_CHANGELOG_FILE_ON_SERVER)

    if changelog_request.status_code != 200:
        logging.error("Can't get app changelog, status code - " + str(changelog_request.status_code))
        raise ConnectionError("Can't get app changelog, status code - " + str(changelog_request.status_code))

    return changelog_request.text


def is_up_to_date() -> bool:
    """Check if newest version is installed."""

    if get_latest_version_id() == appinfo.APP_VERSION_ID:
        logging.info('App is up to date!')
        return True
    else:
        logging.warning('App is not up to date!')
        return False


def download_new_version():
    """Download zip of latest version from server."""

    logging.info('Downloading new app version binaries')

    update_file = open(UPDATE_FILE, 'wb')

    update_file.write(requests.get(appinfo.API_DOMAIN + UPDATE_FILE_ON_SERVER).content)

    update_file.close()


def backup_all():
    """Backup app files."""

    logging.info('Making an backup')

    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)

    for file in os.listdir('.'):
        if BACKUP_FOLDER not in file:
            if os.path.isdir(file):
                shutil.copytree(file, BACKUP_FOLDER + '/' + file)
            else:
                shutil.copy2(file, BACKUP_FOLDER)


def remove_old_installation():
    """Remove old files."""

    logging.info('Removing old app installation')

    for file in os.listdir('.'):
        if BACKUP_FOLDER not in file:
            if os.path.isdir(file):
                shutil.rmtree(file)
            else:
                os.remove(file)


def extract_new_version():
    """Extract files from archive."""

    logging.info('Unzipping new version')

    update_file = ZipFile(UPDATE_FILE, 'r')
    update_file.extractall('.')
    update_file.close()


def restore_backup():
    """Copy files from backup to folder."""

    logging.info('Restoring from last backup')

    for file in os.listdir(BACKUP_FOLDER):
        if os.path.isdir(BACKUP_FOLDER + '/' + file):
            shutil.copytree(BACKUP_FOLDER + '/' + file, file)
        else:
            shutil.copy2(BACKUP_FOLDER + '/' + file, '.')


def delete_update_archive():
    logging.debug('Removing update archive')
    os.remove(UPDATE_FILE)


def delete_backup_folder():
    logging.debug('Removing backup')
    shutil.rmtree(BACKUP_FOLDER)


class Updater(threading.Thread):
    """Downloads new version and installs it."""

    cancel = False
    status = 'Начинаем...'

    def run(self):
        """Begin updating."""

        logging.info("Update started")

        if is_up_to_date():
            logging.critical('Already up to date')
            raise ValueError('Already up to date')

        self.status = 'Downloading update...'

        download_new_version()

        if self.cancel:
            logging.info('Canceling update')
            self.status = 'Removing update files...'
            delete_update_archive()
            return

        self.status = 'Creating backup...'

        backup_all()

        if self.cancel:
            logging.info('Canceling update')
            self.status = 'Removing update files...'
            delete_update_archive()
            delete_backup_folder()
            return

        self.status = 'Removing old installation...'

        remove_old_installation()

        if self.cancel:
            logging.info('Canceling update')
            self.status = 'Restoring old version...'
            restore_backup()
            self.status = 'Removing update files...'
            delete_update_archive()
            delete_backup_folder()
            return

        self.status = 'Installing new update...'

        extract_new_version()

        if self.cancel:
            logging.info('Canceling update')
            self.status = 'Removing update files...'
            remove_old_installation()
            self.status = 'Restoring old version...'
            restore_backup()
            self.status = 'Removing update files...'
            delete_update_archive()
            delete_backup_folder()
            return

        logging.info('Update finished')

        self.status = 'Removing update files...'

        delete_update_archive()
        delete_backup_folder()

        logging.info('Cleaned, exiting from thread')
