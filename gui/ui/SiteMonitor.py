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

from PyQt5 import QtWidgets, QtCore
from gui.ui import monitor
from gui.ui.SiteAdd import SiteAdd
from gui.ui.SiteSettings import SiteSettings
from api.gui import *
from api import sites
from app import site
import logging as log


class SiteMonitor(QtWidgets.QDialog, monitor.Ui_Dialog):
    def __init__(self):
        self.sites = site.get_sites_dict()

        log.info('Initializing SiteMonitor window')
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('SiteMonster - SiteMonitor')
        set_wnd_icon(self, 'logo.ico')

        self.timer = QtCore.QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.check_sites_file)
        self.timer.start()

        self.fav_btn_example.hide()
        self.description_.hide()
        self.fav_only_checkbox.hide()
        self.settings_btn.hide()
        self.site_settings.hide()
        self.delete_site.hide()

        log.debug('Building sites list')
        if site.get_sites_dict().keys().__len__() > 0:
            for key in self.sites:
                if True:
                    self.fav_sites = QtWidgets.QPushButton(self.fav_container_)
                    self.fav_container.addWidget(self.fav_sites)
                    self.fav_sites.setObjectName(key)

                    self.fav_sites.setToolTip(key)
                    self.fav_sites.setToolTipDuration(20 * 100)

                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(self.sites[key]['favicon']),
                                   QtGui.QIcon.Normal, QtGui.QIcon.Off)

                    self.fav_sites.setIcon(icon)
                    self.fav_sites.setIconSize(QtCore.QSize(24, 24))
                    self.fav_sites.setMaximumSize(QtCore.QSize(256, 32))
                    self.fav_sites.clicked.connect(self.make_get_site_info(key))
                    # self.fav_sites.setText(key)

                    self.fav_container.addWidget(self.fav_sites)
                    if not self.sites[key]['favourite']:
                        self.fav_sites.hide()
            self.add_site_btn.hide()
            self.message_label.setText("Select site from list.")

        self.add_site_btn.clicked.connect(self.add_site_onclick)
        self.plus_site.clicked.connect(self.add_site_onclick)
        self.menu_btn.clicked.connect(self.menu_onclick)
        self.fav_only_checkbox.stateChanged.connect(self.filter)
        self.site_settings.clicked.connect(self.site_settings_onclick)
        self.delete_site.clicked.connect(self.site_delete)

    def check_sites_file(self):
        log.debug('Checking siteList.json for changes')
        if self.sites == site.get_sites_dict():
            pass
        else:
            self.timer.stop()
            self.window = SiteMonitor()
            self.window.setGeometry(self.geometry())
            self.window.show()
            self.close()

    def add_site_onclick(self):
        log.info('Opening SiteAdd window')
        self.site_add_wnd = SiteAdd()
        geometry = self.geometry()
        self.site_add_wnd.show()
        self.site_add_wnd.setGeometry(geometry)

    def make_get_site_info(self, name: str):
        def get_site_info():
            log.debug('Getting info about \'' + name + '\'')
            self.site = name
            self.message_label.setText('Info about [SITENAME]'.replace('[SITENAME]', name))
            self.description_.show()
            self.url.setText(self.sites[name]['url'])
            self.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
            self.status.setText("OK" if sites.check(self.sites[name]) else "OOPS")
            self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.site_settings.show()
            self.delete_site.show()

        return get_site_info

    def menu_onclick(self):
        state: bool = not self.menu_btn.property('state')
        self.menu_btn.setProperty('state', state)

        tmp: int = 2
        if state:
            self.fav_only_checkbox.show()
        else:
            self.fav_only_checkbox.hide()
        for fav_site in self.fav_container_.children():
            if tmp > 0:
                tmp -= 1
                continue
            if state:
                fav_site.setText(fav_site.objectName())
            else:
                fav_site.setText('')

    def filter(self):
        log.debug('Filtering list of sites')
        state = self.fav_only_checkbox.checkState()
        tmp: int = 2
        for siteobj in self.fav_container_.children():
            if tmp > 0:
                tmp -= 1
                continue
            if not self.sites[siteobj.objectName()]["favourite"]:
                if state:
                    siteobj.hide()
                else:
                    siteobj.show()

    def site_settings_onclick(self):
        log.info('Opening SiteSettings window about \'' + self.site + '\'')
        geometry = self.geometry()
        self.settings = SiteSettings({'site_name': self.site})
        self.settings.setGeometry(geometry)
        self.settings.show()

    def site_delete(self):
        log.info('Deleting site \'' + self.site + '\'')
        name = self.site
        if QtWidgets.QMessageBox().question(self, 'Really', 'Are you sure to delete ' + name + '?',
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                            QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes:
            site.delete(name)
