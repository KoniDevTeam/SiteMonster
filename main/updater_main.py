import sys

from api import osinfo

from PyQt5.QtWidgets import QApplication

from gui.update_tool import UpdateToolWindow

if __name__ == '__main__':
    osinfo.init_log('updater')
    osinfo.log_pc_info()
    app = QApplication(sys.argv)
    updater_window = UpdateToolWindow(app.primaryScreen().size())
    app.exec_()
