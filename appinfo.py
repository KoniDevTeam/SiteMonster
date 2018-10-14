"""App info."""
from api.files import get_and_create_data_folder, get_media_folder_path

PID_FILE = get_and_create_data_folder() + '/' + 'daemon_pid.tmp'

APP_NAME = 'Site Monster'
APP_ICON = get_media_folder_path() + '/' + 'logo.ico'
APP_VERSION = 'v1.0'
APP_VERSION_ID = 0
UPDATER_VERSION_ID = 0

API_DOMAIN = 'http://itgrusha.com'