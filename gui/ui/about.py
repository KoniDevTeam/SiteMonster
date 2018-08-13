# Copyright (C) 2018 Koni Dev Team, All Rights Reserved
# https://github.com/KoniDevTeam/SiteMonster/
#
# This file is part of Site Monster.
#
# Site Monster is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Site Monster is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Site Monster.  If not, see <https://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/about.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(24)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.verticalLayout.addWidget(self.header)
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.text.setFont(font)
        self.text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text.setWordWrap(True)
        self.text.setOpenExternalLinks(True)
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.card1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.card1.setFont(font)
        self.card1.setAlignment(QtCore.Qt.AlignCenter)
        self.card1.setOpenExternalLinks(True)
        self.card1.setObjectName("card1")
        self.verticalLayout.addWidget(self.card1)
        self.card2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.card2.setFont(font)
        self.card2.setAlignment(QtCore.Qt.AlignCenter)
        self.card2.setOpenExternalLinks(True)
        self.card2.setObjectName("card2")
        self.verticalLayout.addWidget(self.card2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "SiteMonster"))
        self.text.setText(_translate("MainWindow", "Site Monster - приложение для администраторов сайтов, которое мгновенно сообщит вам если ваш сайт упал. Данное приложение разрабывается нами - молодой и перспективной командой разработчиков Koni Dev Team. Мы рабоатет что бы улучшить это приложение, сделать его стабильным и еще более полезным. Вы можете помочь нам, исправляя баги или создовая новые функции на странице нашего проекта <a href=\"https://github.com/Nekit10/SiteMonster\">GitHub</a>. Или вы можете пожертвовать деньги на разроботку. Для этого отпарвьте деньги на одну из следущих карт с подписью На разроботку Site Monster:"))
        self.card1.setText(_translate("MainWindow", "5168 7426 0366 3885"))
        self.card2.setText(_translate("MainWindow", "5168 7559 0124 1956"))
