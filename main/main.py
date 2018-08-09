import sys
import logging

from PyQt5 import QtWidgets

from gui.ui.SiteMonster import SiteMonster
from api import osinfo


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
