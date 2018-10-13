"""App info."""
from api.files import get_and_create_data_folder

PID_FILE = get_and_create_data_folder() + '/' + 'daemon_pid.tmp'

APP_NAME = 'Site Monster'
APP_ICON = '../media/logo.ico'  # Ну так надо
APP_VERSION = 'v1.0'
APP_VERSION_ID = 0
UPDATER_VERSION_ID = 0

API_DOMAIN = 'http://itgrusha.com'