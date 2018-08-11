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

from PyQt5 import QtWidgets
from gui.ui import welcome as design
from gui.ui.SiteMonitor import SiteMonitor
from api.gui import *


class SiteMonster(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Welcome")
        set_wnd_icon(self, 'logo.ico')

        self.start_btn.clicked.connect(self.start_btn_onclick)
        self.quit_btn.clicked.connect(self.quit)

    def start_btn_onclick(self):
        self.window = SiteMonitor()
        self.window.setGeometry(self.geometry())
        self.window.show()
        self.close()

    def quit(self):
        reply = QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to quit?', QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.close()
        else:
            pass
