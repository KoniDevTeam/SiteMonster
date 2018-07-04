"""App info."""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QFont

import appinfo


class InfoWindow(QWidget):

    screen_size = None

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 500

    def __init__(self, screen_size):
        """Init window

        Get screen_size by app.primaryScreen().size() where app is your QApplication

        """

        super().__init__()

        self.screen_size = screen_size

        self.initUI()

    def initUI(self):
        """Create and setup gui elements."""

        self.setGeometry((self.screen_size.width() - self.WINDOW_WIDTH) / 2,
                         (self.screen_size.height() - self.WINDOW_HEIGHT) / 2, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle(appinfo.APP_NAME + ' Info')
        self.setWindowIcon(QIcon(appinfo.APP_ICON))
        self.setFixedSize(self.size())



        self.show()
