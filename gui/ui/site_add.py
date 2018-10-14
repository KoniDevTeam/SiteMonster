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

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(20)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setInputMethodHints(QtCore.Qt.ImhPreferLatin)
        self.name.setInputMask("")
        self.name.setText("")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setClearButtonEnabled(True)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.url_container = QtWidgets.QHBoxLayout()
        self.url_container.setSpacing(12)
        self.url_container.setObjectName("url_container")
        self.url_label = QtWidgets.QLabel(Dialog)
        self.url_label.setAlignment(QtCore.Qt.AlignCenter)
        self.url_label.setObjectName("url_label")
        self.url_container.addWidget(self.url_label)
        self.url = QtWidgets.QLineEdit(Dialog)
        self.url.setInputMethodHints(QtCore.Qt.ImhPreferLatin)
        self.url.setInputMask("")
        self.url.setText("")
        self.url.setAlignment(QtCore.Qt.AlignCenter)
        self.url.setClearButtonEnabled(True)
        self.url.setObjectName("url")
        self.url_container.addWidget(self.url)
        self.verticalLayout.addLayout(self.url_container)
        self.continue_btn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.continue_btn.setFont(font)
        self.continue_btn.setObjectName("continue_btn")
        self.verticalLayout.addWidget(self.continue_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.cancel = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.verticalLayout.addWidget(self.cancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.name, self.url)
        Dialog.setTabOrder(self.url, self.continue_btn)
        Dialog.setTabOrder(self.continue_btn, self.cancel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name_label.setText(_translate("Dialog", "Let`s give your site a name"))
        self.name.setPlaceholderText(_translate("Dialog", "Say hello to ..."))
        self.url_label.setText(_translate("Dialog", "Enter its URL"))
        self.url.setPlaceholderText(_translate("Dialog", "It will be accsessible via ..."))
        self.continue_btn.setText(_translate("Dialog", "Continue"))
        self.cancel.setText(_translate("Dialog", "Cancel"))

