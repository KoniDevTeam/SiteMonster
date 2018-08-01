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

        name = QLabel(appinfo.APP_NAME, self)
        name.setGeometry(int((self.WINDOW_WIDTH - 260)/2), 0, 260, 50)
        name.setFont(QFont(name.font().family(), 32, QFont.AnyStyle))

        name = QLabel('Site Monster - приложение для администраторов сайтов, которое мгновенно сообщит вам если \n'
                      'ваш сайт упал. Данное приложение разрабывается нами - молодой и перспективной командой \n'
                      'разработчиков Koni Dev Team. Мы рабоатет что бы улучшить это приложение, сделать его \n'
                      'стабильным и еще более полезным. Вы можете помочь нам, исправляя баги или создовая \n'
                      'новые функции на github (Подробнее: https://github.com/Nekit10/SiteMonster). Или \n'
                      'вы можете пожертвовать деньги на разроботку. Для этого отпарвьте деньги на одну \n'
                      'из следущих карт с подписью \'На разроботку Site Monster\':\n'
                      '5168 7426 0366 3885\n'
                      '5168 7559 0124 1956\n', self)
        name.setGeometry(int((self.WINDOW_WIDTH - 600)/2), 60, 750, 300)

        self.show()