from PyQt5 import QtWidgets, QtCore
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
