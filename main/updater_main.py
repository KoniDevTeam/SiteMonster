import sys
import logging

from PyQt5.QtWidgets import QApplication

from gui.update_tool import UpdateToolWindow
from api import osinfo
from app import logger

if __name__ == '__main__':
    logger.init_log('updater')
    logger.log_pc_info()
    app = QApplication(sys.argv)
    updater_window = UpdateToolWindow(app.primaryScreen().size())

    logging.info('Starting updater')

    app.exec_()
