import sys
from PyQt5 import QtWidgets
import gui.ui.welcome as design
from gui.ui import monitor
import gui.site_settings_edit
from PyQt5.QtCore import QCoreApplication


class settings_edit(QtWidgets.QDialog, gui.site_settings_edit.SiteSettingsEditWindow):
    def __init__(self):
        super().__init__()
        self.initUI(self)


class Monitor(QtWidgets.QDialog, monitor.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_site_btn.clicked.connect(self.add_site_onclick)

    def add_site_onclick(self):
        self.settings_window("Hello", self.size())
        x, y = self.x(), self.y()
        h, w = self.height(), self.width()
        self.settings_window.show()
        #self.window.hide()
        #self.settings_window.move(x, y)
        #self.settings_window.resize(w, h)


class SiteMonster(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_btn.clicked.connect(self.start_btn_onclick)
        self.quit_btn.clicked.connect(self.quit)

    def start_btn_onclick(self):
        #app = QtWidgets.QApplication(sys.argv)
        self.window = Monitor()
        x, y = self.x(), self.y()
        h, w = self.height(), self.width()
        self.window.show()
        self.hide()
        self.window.move(x , y)
        self.window.resize(w, h)
        #sys.exit(app.exec_())

    def quit(self):
        self.close()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtWidgets.QMessageBox.Yes |
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
    main()
