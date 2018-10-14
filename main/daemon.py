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

import time
from logapi import logging_daemon as logging
import os
import sys
from threading import Thread

from PyQt5.QtWidgets import QSystemTrayIcon, QApplication, QAction, QMenu, QMainWindow
from PyQt5 import QtGui

import app.notifications as notify
from app import site
from api import sites
from api import files
import appinfo

is_running = True

start_action = None
stop_action = None
app = None


def save_pid():
    f = open(appinfo.PID_FILE, 'w')
    f.write(str(os.getpid()))
    f.close()


def check_site(name: str, site_data: dict):
    if not sites.check(site_data):
        fail_actions = site_data['settings']['fail_actions']
        if fail_actions['send_notification']:
            logging.warning('Site %s is down!!!' % name)
            notify.send_notification('Site %s is down!!!' % name)
        #if fail_actions['play_sound']:
        if True:
            logging.warning('Playing sound!')
            notify.play_sound()
        time.sleep(30)


def start():
    global is_running, start_action, stop_action
    is_running = True
    start_action.setEnabled(False)
    stop_action.setEnabled(True)


def stop():
    global is_running, start_action, stop_action
    is_running = False
    start_action.setEnabled(True)
    stop_action.setEnabled(False)


def check():
    if is_running:
        sites_dict = site.get_sites_dict()
        for i, j in sites_dict.items():
            logging.info("Checking " + i)
            check_site(i, j)
        time.sleep(1)


def close_all():
    app.quit()
    exit(0)


if __name__ == '__main__':
    save_pid()
    app = QApplication(sys.argv)
    # Init QSystemTrayIcon
    window = QMainWindow(None)
    tray_icon = QSystemTrayIcon(window)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(appinfo.APP_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    tray_icon.setIcon(icon
                      )
    start_action = QAction("Start", window)
    stop_action = QAction("Stop", window)
    exit_action = QAction("Exit", window)
    start_action.setEnabled(False)

    start_action.triggered.connect(start)
    stop_action.triggered.connect(stop)
    exit_action.triggered.connect(close_all)

    tray_menu = QMenu()
    tray_menu.addAction(start_action)
    tray_menu.addAction(stop_action)
    tray_menu.addAction(exit_action)

    tray_icon.setContextMenu(tray_menu)
    tray_icon.show()

    thread1 = Thread(target=check)
    thread1.daemon = True

    thread1.start()

    app.exec_()

    thread1.join()
