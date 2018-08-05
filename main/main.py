import sys
import json
import logging

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from app import site
from api import sites
from gui.ui import monitor, site_settings, addsite
import gui.ui.welcome as design
from api import osinfo


class SiteSettings(QtWidgets.QDialog, site_settings.Ui_Dialog):
    def __init__(self, data=None):
        super().__init__()
        if data is None:
            data = {}
        self.setupUi(self)

        self.quit.clicked.connect(self.exit)
        self.save.clicked.connect(self.save_all)

        self.site_name = data['site_name']
        self.setWindowTitle('Settings: ' + self.site_name)
        self.header.setText(self.header.text().replace('[SITENAME]', self.site_name))

        website = site.get_sites_dict()[self.site_name]

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

        self.notification.setChecked(website['settings']['fail_actions']['send_notification'])
        self.sound.setChecked(website['settings']['fail_actions']['play_sound'])

        self.text_edits = [self.http_method, self.http_headers, self.http_body, self.http_proxy, self.https_proxy,
                           self.http_codes, self.expected, self.notification, self.sound]

    def exit(self):
        if QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                          QtWidgets.QMessageBox.No) ==\
                QtWidgets.QMessageBox.Yes:
            self.close()

    def save_all(self):
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
        self.close()


class SiteAdd(QtWidgets.QDialog, addsite.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cancel.clicked.connect(self.quit)
        self.continue_btn.clicked.connect(self.continue_f)

    def continue_f(self):
        if len(self.name.text()) > 3:
            if self.name.text() not in site.get_sites_dict().keys():
                if len(self.url.text()) > 2:
                    site.add(self.name.text(), self.url.text(), site.build_settings())
                    self.settings_window = SiteSettings({'site_name': self.name.text()})
                    geometry = self.geometry()
                    self.settings_window.setGeometry(geometry)
                    self.settings_window.show()
                    self.hide()
            else:
                QtWidgets.QMessageBox.information(self, 'Message', 'Name must be unique',
                                                  QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, 'Message', 'Name must be at least 4 characters long',
                                              QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

        # self.closeEvent()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to cancel?', QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def quit(self):
        self.close()


class Monitor(QtWidgets.QDialog, monitor.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.fav_btn_example.hide()
        self.description_.hide()
        self.fav_only_checkbox.hide()

        if site.get_sites_dict().keys().__len__() > 0:
            self.sites = site.get_sites_dict()
            for key in self.sites:
                if True:
                    self.fav_sites = QtWidgets.QPushButton(self.fav_container_)
                    self.fav_container.addWidget(self.fav_sites)
                    self.fav_sites.setObjectName(key)

                    self.fav_sites.setToolTip(key)
                    self.fav_sites.setToolTipDuration(20 * 100)

                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("../media/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                    self.fav_sites.setIcon(icon)
                    self.fav_sites.setIconSize(QtCore.QSize(24, 24))
                    self.fav_sites.setMaximumSize(QtCore.QSize(256, 32))
                    self.fav_sites.clicked.connect(self.make_get_site_info(key))
                    # self.fav_sites.setText(key)

                    self.fav_container.addWidget(self.fav_sites)
                    if not self.sites[key]['favourite']:
                        self.fav_sites.hide()
            self.add_site_btn.hide()
            self.message_label.setText("Select site from list or Favourites")

        self.add_site_btn.clicked.connect(self.add_site_onclick)
        self.menu_btn.clicked.connect(self.menu_onclick)
        self.fav_only_checkbox.stateChanged.connect(self.filter)

    def add_site_onclick(self):
        self.site_add_wnd = SiteAdd()
        geometry = self.geometry()
        self.site_add_wnd.show()
        self.site_add_wnd.setGeometry(geometry)

    def make_get_site_info(self, name: str):
        def get_site_info():
            self.message_label.setText('Info about [SITENAME]'.replace('[SITENAME]', name))
            self.description_.show()
            self.url.setText(self.sites[name]['url'])
            self.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
            self.status.setText("OK" if sites.check(self.sites[name]) else "OOPS")
            self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        return get_site_info

    def menu_onclick(self):
        state: bool = not self.menu_btn.property('state')
        self.menu_btn.setProperty('state', state)
        # print('Hell`o')
        tmp: int = 2
        if state:
            self.fav_only_checkbox.show()
        else:
            self.fav_only_checkbox.hide()
        for fav_site in self.fav_container_.children():
            if tmp > 0:
                tmp -= 1
                continue
            # print(fav_site.objectName())
            if state:
                fav_site.setText(fav_site.objectName())
            else:
                fav_site.setText('')
                # self.fav_container.removeWidget(fav_site)  # terrible thing

    def filter(self):
        state = self.fav_only_checkbox.checkState()
        tmp: int = 2
        for siteobj in self.fav_container_.children():
            if tmp > 0:
                tmp -= 1
                continue
            if not self.sites[siteobj.objectName()]["favourite"]:
                print(siteobj.objectName())
                if state:
                    siteobj.hide()
                else:
                    siteobj.show()


class SiteMonster(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_btn.clicked.connect(self.start_btn_onclick)
        self.quit_btn.clicked.connect(self.quit)

    def start_btn_onclick(self):
        self.window = Monitor()
        size = self.size()
        x, y = self.x(), self.y()
        self.window.show()
        self.hide()
        self.window.move(x , y)
        self.window.resize(size)

    def quit(self):
        self.close()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to quit?', QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = SiteMonster()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    osinfo.init_log('app')
    osinfo.log_pc_info()
    logging.info('Starting app')
    main()
