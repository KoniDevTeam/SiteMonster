"""App info."""
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

import appinfo
from api import updates


class UpdateToolWindow(QWidget):

    screen_size = None

    updater = None
    statusLabel = None

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 500

    def check(self):
        """Update status label."""
        print(self.updater)
        if self.updater is not None:
            self.statusLabel.setText(self.updater.status)

    def __init__(self, screen_size):
        """Init window

        Get screen_size by app.primaryScreen().size() where app is your QApplication

        """

        super().__init__()

        self.screen_size = screen_size

        self.initUI()

        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.check)
        self.timer.start()

    def begin(self):
        """Begin updating."""

        if self.updater is None:
            self.updater = updates.Updater()
            self.updater.start()

    def cancel(self):
        """Cancel updating."""

        if self.updater is not None:
            self.updater.cancel = True

    def initUI(self):
        """Create and setup gui elements."""

        self.setGeometry((self.screen_size.width() - self.WINDOW_WIDTH) / 2,
                         (self.screen_size.height() - self.WINDOW_HEIGHT) / 2, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle(appinfo.APP_NAME + ' Info')
        self.setWindowIcon(QIcon(appinfo.APP_ICON))
        self.setFixedSize(self.size())

        version_label = QLabel('Ваша версия: ' + appinfo.APP_VERSION, self)
        version_label.setGeometry(30, 30, 120, 40)

        new_version_label = QLabel('Дотсупная версия: ' + updates.get_latest_version_name(), self)
        new_version_label.setGeometry(30, 90, 160, 40)

        changelog_label = QLabel('В новой версии: \n' + updates.get_changelog(), self)
        changelog_label.setGeometry(300, 10, 200, 250)

        status_label = QLabel('', self)
        status_label.setGeometry(30, 150, 120, 40)
        self.statusLabel = status_label

        start_btn = QPushButton('Установить', self)
        start_btn.clicked.connect(self.begin)
        start_btn.setGeometry(30, 300, 200, 100)

        cancel_btn = QPushButton('Отменить', self)
        cancel_btn.clicked.connect(self.cancel)
        cancel_btn.setGeometry(330, 300, 200, 100)

        self.show()
