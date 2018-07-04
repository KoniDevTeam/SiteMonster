"""App update tool."""

import os
import shutil
import threading
from zipfile import ZipFile

import requests

import appinfo

VERSION_ID_FILE_ON_SERVER = '/Site Monster/version'
UPDATE_FILE_ON_SERVER = '/Site Monster/latest.zip'
UPDATE_FILE = 'latest.zip'
BACKUP_FOLDER = 'backup'


def get_latest_version_id():
    """Get id of latest vresion from server."""

    version_request = requests.get(appinfo.API_DOMAIN + VERSION_ID_FILE_ON_SERVER)

    if version_request.status_code != 200:
        raise ConnectionError("Can't get app version, status code - " + str(version_request.status_code))

    return int(version_request.text)


def is_up_to_date() -> bool:
    """Check if newest version is installed."""

    return get_latest_version_id() == appinfo.APP_VERSION_ID


def download_new_version():
    """Download zip of latest version from server."""

    update_file = open(UPDATE_FILE, 'wb')

    update_file.write(requests.get(appinfo.API_DOMAIN + UPDATE_FILE_ON_SERVER).content)

    update_file.close()


def backup_all():
    """Backup app files."""

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

    for file in os.listdir('.'):
        if BACKUP_FOLDER not in file:
            if os.path.isdir(file):
                shutil.rmtree(file)
            else:
                os.remove(file)


def extract_new_version():
    """Extract files from archive."""

    update_file = ZipFile(UPDATE_FILE, 'r')
    update_file.extractall('.')
    update_file.close()


def restore_backup():
    """Copy files from backup to folder."""

    for file in os.listdir(BACKUP_FOLDER):
        if os.path.isdir(BACKUP_FOLDER + '/' + file):
            shutil.copytree(BACKUP_FOLDER + '/' + file, file)
        else:
            shutil.copy2(BACKUP_FOLDER + '/' + file, '.')


def delete_update_archive():
    os.remove(UPDATE_FILE)


def delete_backup_folder():
    shutil.rmtree(BACKUP_FOLDER)


class Updater(threading.Thread):
    """Downloads new version and installs it."""

    cancel = False

    def run(self):
        """Begin updating."""

        if is_up_to_date():
            raise ValueError('Already up to date')

        download_new_version()

        if self.cancel:
            delete_update_archive()
            return

        backup_all()

        if self.cancel:
            delete_update_archive()
            delete_backup_folder()
            return

        remove_old_installation()

        if self.cancel:
            restore_backup()
            delete_update_archive()
            delete_backup_folder()
            return

        extract_new_version()

        delete_update_archive()
        delete_backup_folder()
