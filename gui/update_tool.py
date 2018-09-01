"""App info."""

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

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

import appinfo
from api import updates


class UpdateToolWindow(QWidget):

    screen_size = None

    updater = None
    statusLabel = None

    WINDOW_WIDTH = 555
    WINDOW_HEIGHT = 430

    def check(self):
        """Update status label."""
        if self.updater is not None:
            self.statusLabel.setText(self.updater.status)

    def __init__(self, screen_size):
        """Init window

        Get screen_size by app.primaryScreen().size() where app is your QApplication

        """

        logging.info('Starting update tool window')

        super().__init__()

        self.screen_size = screen_size

        self.initUI()

        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.check)
        self.timer.start()

    def begin(self):
        """Begin updating."""

        if self.updater is None:
            self.updater = updates.Updater()
            self.updater.start()

    def cancel(self):
        """Cancel updating."""

        logging.debug('Canceling update')

        if self.updater is not None:
            self.updater.cancel = True
            self.updater.join()
        sys.exit()

    def initUI(self):
        """Create and setup gui elements."""

        self.setGeometry((self.screen_size.width() - self.WINDOW_WIDTH) / 2,
                         (self.screen_size.height() - self.WINDOW_HEIGHT) / 2, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle(appinfo.APP_NAME + ' Updating')
        self.setWindowIcon(QIcon(appinfo.APP_ICON))
        self.setFixedSize(self.size())

        version_label = QLabel('App version: ' + appinfo.APP_VERSION, self)
        version_label.setGeometry(30, 30, 120, 40)

        new_version_label = QLabel('New version: ' + updates.get_latest_version_name(), self)
        new_version_label.setGeometry(30, 90, 160, 40)

        changelog_label = QLabel("What's new: \n" + updates.get_changelog(), self)
        changelog_label.setGeometry(300, 10, 200, 250)

        status_label = QLabel('', self)
        status_label.setGeometry(30, 150, 120, 40)
        self.statusLabel = status_label

        start_btn = QPushButton('Install', self)
        start_btn.clicked.connect(self.begin)
        start_btn.setGeometry(30, 300, 200, 100)

        cancel_btn = QPushButton('Cancel', self)
        cancel_btn.clicked.connect(self.cancel)
        cancel_btn.setGeometry(330, 300, 200, 100)

        self.show()
