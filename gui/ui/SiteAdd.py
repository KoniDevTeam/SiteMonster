from PyQt5 import QtWidgets
from gui.ui import site_add
from gui.ui.SiteSettings import SiteSettings
from api.gui import *
from app import site


class SiteAdd(QtWidgets.QDialog, site_add.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('SiteMonster - add site')
        set_wnd_icon(self, 'plus.png')

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
