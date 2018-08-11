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

import json

from PyQt5 import QtWidgets
from gui.ui import site_settings
from api.gui import *
from app import site
import logging as log


class SiteSettings(QtWidgets.QDialog, site_settings.Ui_Dialog):
    def __init__(self, data=None):
        log.info('Initializing SiteSettings window')
        super().__init__()
        if data is None:
            data = {}
        self.setupUi(self)

        self.label.hide()

        set_wnd_icon(self, 'settings.png')

        self.quit.clicked.connect(self.exit)
        self.save.clicked.connect(self.save_all)

        self.site_name = data['site_name']
        self.setWindowTitle('Settings: ' + self.site_name)
        self.header.setText(self.header.text().replace('[SITENAME]', self.site_name))

        website = site.get_sites_dict()[self.site_name]

        log.debug('Getting site settings')

        text = website['settings']['method']
        self.http_method.setText(text)

        text = website['settings']['headers']
        if text is None:
            text = dict()
        self.http_headers.setText(json.dumps(text))

        text = website['settings']['body']
        self.http_body.setPlainText(text)

        text = website['settings']['proxy']
        if text is None:
            text = {'http': '', 'https': ''}
        self.http_proxy.setText(text['http'])
        self.https_proxy.setText(text['https'])

        text = website['settings']['expected_code']
        if text is None:
            text = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]
        self.http_codes.setText(','.join(str(i) for i in text))

        text = website['settings']['expected_answer']
        if text is None:
            text = ''
        self.expected.setText(text)

        text = website['favourite']
        if text is None:
            text = False
        self.favourite.setChecked(text)

        self.notification.setChecked(website['settings']['fail_actions']['send_notification'])
        self.sound.setChecked(website['settings']['fail_actions']['play_sound'])

        self.text_edits = [self.http_method, self.http_headers, self.http_body, self.http_proxy, self.https_proxy,
                           self.http_codes, self.expected, self.notification, self.sound, self.favourite]

    def exit(self):
        log.info('Closing window')
        if QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                          QtWidgets.QMessageBox.No) ==\
                QtWidgets.QMessageBox.Yes:
            self.close()

    def save_all(self):
        log.info('Saving changed settings')
        proxy = None
        if self.text_edits[3].text() != '' or self.text_edits[4].text() != '':
            proxy = {'http': self.text_edits[3].text(), 'https': self.text_edits[4].text()}

        site.change_settings(self.site_name,
                             site.build_settings(self.text_edits[0].text(),
                                                 json.loads(self.text_edits[1].text()),
                                                 self.text_edits[2].toPlainText(),
                                                 proxy,
                                                 list(int(i) for i in self.text_edits[5].text().split(',')),
                                                 self.text_edits[6].text(),
                                                 site.build_fail_actions(self.text_edits[7].isChecked(),
                                                                         self.text_edits[8].isChecked()))
                             )
        site.set_favourite(self.site_name, self.text_edits[9].isChecked())

        self.close()
