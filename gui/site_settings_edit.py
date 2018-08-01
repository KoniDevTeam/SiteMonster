"""Editing site's settings."""

import json

from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QGridLayout, QCheckBox, QPushButton
from PyQt5.QtGui import QIcon

import appinfo
from app import site


class SiteSettingsEditWindow(QWidget):

    site_name = ''
    screen_size = None

    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500

    text_edits = []

    def __init__(self, site_name, screen_size):
        """Init window

        Get screen_size by app.primaryScreen().size() where app is your QApplication

        """

        super().__init__()

        self.site_name = site_name
        self.screen_size = screen_size

        self.initUI()

    def save_all(self):
        proxy = None
        if self.text_edits[3].text() != '' or self.text_edits[4].text() != '':
            proxy = {'http': self.text_edits[3].text(), 'https': self.text_edits[4].text()}
        site.change_settings(self.site_name,
                             site.build_settings(self.text_edits[0].text(),
                                                 json.loads(self.text_edits[1].text()),
                                                 self.text_edits[2].text(),
                                                 proxy,
                                                 list(int(i) for i in self.text_edits[5].text().split(',')),
                                                 self.text_edits[6].text(),
                                                 site.build_fail_actions(self.text_edits[7].isChecked(),
                                                                         self.text_edits[8].isChecked()))
                             )

    def initUI(self):
        """Create and setup gui elements."""

        grid = QGridLayout()
        self.setLayout(grid)

        self.setGeometry((self.screen_size.width() - self.WINDOW_WIDTH) / 2, (self.screen_size.height() - self.WINDOW_HEIGHT) / 2, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle('Settings: ' + self.site_name)
        self.setWindowIcon(QIcon(appinfo.APP_ICON))
        self.setMinimumHeight(400)

        website = site.get_sites_list()[self.site_name]

        test1 = QLabel('Как заполнять: <тут на докуменацию ссылка>', self)
        test1.setGeometry(0, 0, 1000, 20)

        grid.addWidget(QLabel('HTTP method:'), 0, 0)
        grid.addWidget(QLabel('HTTP headers:'), 1, 0)
        grid.addWidget(QLabel('HTTP data:'), 2, 0)
        grid.addWidget(QLabel('Proxies HTTP:'), 3, 0)
        grid.addWidget(QLabel('Proxies HTTPS:'), 4, 0)
        grid.addWidget(QLabel('Предполгаемые коды состояния HTTP (через запятую):'), 5, 0)
        grid.addWidget(QLabel('Предполгаемый ответ сервера:'), 6, 0)

        method_line = QLineEdit()
        text = website['settings']['method']
        method_line.setText(text)
        grid.addWidget(method_line, 0, 1)

        headers_line = QLineEdit()
        text = website['settings']['headers']
        if text is None:
            text = dict()
        headers_line.setText(json.dumps(text))
        grid.addWidget(headers_line, 1, 1)

        body_line = QLineEdit()
        text = website['settings']['body']
        body_line.setText(text)
        grid.addWidget(body_line, 2, 1)

        proxy_line = QLineEdit()
        text = website['settings']['proxy']
        if text is None:
            text = {'http': ''}
        proxy_line.setText(text['http'])
        grid.addWidget(proxy_line, 3, 1)

        proxy_https_line = QLineEdit()
        text = website['settings']['proxy']
        if text is None:
            text = {'https': ''}
        proxy_https_line.setText(text['https'])
        grid.addWidget(proxy_https_line, 4, 1)

        expected_code_line = QLineEdit()
        text = website['settings']['expected_code']
        if text is None:
            text = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]
        expected_code_line.setText(','.join(str(i) for i in text))
        grid.addWidget(expected_code_line, 5, 1)

        expected_answer_line = QLineEdit()
        text = website['settings']['expected_answer']
        if text is None:
            text = ''
        expected_answer_line.setText(text)
        grid.addWidget(expected_answer_line, 6, 1)

        notif_check = QCheckBox('Если сайт не отвечтает, отправлять уведомление на комптютер')
        notif_check.setChecked(website['settings']['fail_actions']['send_notification'])
        grid.addWidget(notif_check, 7, 0)

        sound_check = QCheckBox('Если сайт не отвечтает, проигрывать звук')
        sound_check.setChecked(website['settings']['fail_actions']['send_notification'])
        grid.addWidget(sound_check, 8, 0)

        self.text_edits = [method_line, headers_line, body_line, proxy_line, proxy_https_line, expected_code_line, expected_answer_line, notif_check, sound_check]

        close_btn = QPushButton('Сохранить')
        close_btn.clicked.connect(self.save_all)
        grid.addWidget(close_btn, 9, 1)

        self.show()
