import sys

from PyQt5.QtWidgets import QApplication

from gui.update_tool import UpdateToolWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    updater_window = UpdateToolWindow(app.primaryScreen().size())
    app.exec_()
