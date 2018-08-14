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

import logging
import sys
import os
import psutil
import platform
import subprocess

from PyQt5 import QtWidgets

from app import logger
from gui.ui.SiteMonster import SiteMonster
from api import osinfo, updates, updater_updates, files


def run(name: str):
    logging.debug('Running ' + name)
    if osinfo.is_win():
        subprocess.Popen([os.path.dirname(sys.executable) + '/' + name + '.exe'])
    elif osinfo.is_linux():
        subprocess.Popen([os.path.dirname(sys.executable) + '/' + name ])
    else:
        raise OSError(platform.system() + 'is not supported!')


def run_daemon():
    try:
        run('daemon')
    except Exception as e:
        logging.error("Can't start daemon: " + str(e))


def run_daemon_if_it_is_not_running():
    if not os.path.exists(osinfo.PID_FILE):
        run_daemon()
    else:
        try:
            f = open(osinfo.PID_FILE, 'r')

            pid = int(f.read().strip())

            f.close()

            if not psutil.pid_exists(pid):
                run_daemon()
        except Exception as e:
            logging.error("Can't check pid file of daemon: " + str(e))
            run_daemon()


def test_for_update():
    try:
        if not updates.is_up_to_date():
            if ask_user_for_update():
                run_updater()
                exit(0)
    except Exception as e:
        logging.error("Can't check for updates: " + str(e))


def ask_user_for_update() -> bool:
    button_reply = QtWidgets.QMessageBox.question(QtWidgets.QMessageBox(), 'New update is available',
                                                  'Do you want to install new update now?',
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                  QtWidgets.QMessageBox.No)

    return button_reply == QtWidgets.QMessageBox.Yes


def run_updater():
    run('updater')
    sys.exit()


def update_updater():
    try:
        logging.info('Begging updating.')
        if not updater_updates.is_up_to_date():
            thread = updater_updates.UpdaterUpdater()
            thread.start()
            return thread
        else:
            return None
    except Exception as e:
        logging.error("Can't update updater: " + str(e))


def main():
    app = QtWidgets.QApplication(sys.argv)
    test_for_update()
    thr = update_updater()
    window = SiteMonster()
    window.show()
    if thr is not None:
        thr.join()
    sys.exit(app.exec_())


if __name__ == '__main__':
    logger.init_log('app')
    logger.log_pc_info()
    logging.info('Starting app')
    run_daemon_if_it_is_not_running()
    main()
