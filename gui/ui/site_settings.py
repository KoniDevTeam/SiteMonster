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
        Dialog.resize(640, 531)
        Dialog.setMinimumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setStyleSheet("QCheckBox::indicator {\n"
"    height: 24px;\n"
"    width: 24px;\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"    image: url(../media/checkbox-off.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover{\n"
"    image: url(../media/checkbox-off-hover.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:pressed{\n"
"    image: url(../media/checkbox-off-pressed.png);\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    image: url(../media/checkbox-on.png);\n"
"}\n"
"QCheckBox::indicator:checked:hover{\n"
"    image: url(../media/checkbox-on-hover.png);\n"
"}\n"
"QCheckBox::indicator:checked:pressed{\n"
"    image: url(../media/checkbox-on-pressed.png);\n"
"}\n"
"\n"
"")
        self.formLayout_2 = QtWidgets.QFormLayout(Dialog)
        self.formLayout_2.setHorizontalSpacing(12)
        self.formLayout_2.setVerticalSpacing(8)
        self.formLayout_2.setObjectName("formLayout_2")
        self.header = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(20)
        self.header.setFont(font)
        self.header.setObjectName("header")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.header)
        self.line = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(600, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.http_method_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.http_method_label.setFont(font)
        self.http_method_label.setObjectName("http_method_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.http_method_label)
        self.http_method = QtWidgets.QLineEdit(Dialog)
        self.http_method.setMinimumSize(QtCore.QSize(0, 24))
        self.http_method.setObjectName("http_method")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.http_method)
        self.http_headers_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.http_headers_label.setFont(font)
        self.http_headers_label.setObjectName("http_headers_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.http_headers_label)
        self.http_headers = QtWidgets.QLineEdit(Dialog)
        self.http_headers.setMinimumSize(QtCore.QSize(0, 24))
        self.http_headers.setObjectName("http_headers")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.http_headers)
        self.http_body_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.http_body_label.sizePolicy().hasHeightForWidth())
        self.http_body_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.http_body_label.setFont(font)
        self.http_body_label.setObjectName("http_body_label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.http_body_label)
        self.http_body = QtWidgets.QPlainTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.http_body.sizePolicy().hasHeightForWidth())
        self.http_body.setSizePolicy(sizePolicy)
        self.http_body.setMinimumSize(QtCore.QSize(0, 24))
        self.http_body.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.http_body.setObjectName("http_body")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.http_body)
        self.http_proxy_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.http_proxy_label.sizePolicy().hasHeightForWidth())
        self.http_proxy_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.http_proxy_label.setFont(font)
        self.http_proxy_label.setObjectName("http_proxy_label")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.http_proxy_label)
        self.http_proxy = QtWidgets.QLineEdit(Dialog)
        self.http_proxy.setMinimumSize(QtCore.QSize(0, 24))
        self.http_proxy.setObjectName("http_proxy")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.http_proxy)
        self.https_proxy_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.https_proxy_label.sizePolicy().hasHeightForWidth())
        self.https_proxy_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.https_proxy_label.setFont(font)
        self.https_proxy_label.setObjectName("https_proxy_label")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.https_proxy_label)
        self.https_proxy = QtWidgets.QLineEdit(Dialog)
        self.https_proxy.setMinimumSize(QtCore.QSize(0, 24))
        self.https_proxy.setObjectName("https_proxy")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.https_proxy)
        self.http_codes_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.http_codes_label.setFont(font)
        self.http_codes_label.setObjectName("http_codes_label")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.http_codes_label)
        self.http_codes = QtWidgets.QLineEdit(Dialog)
        self.http_codes.setMinimumSize(QtCore.QSize(0, 24))
        self.http_codes.setObjectName("http_codes")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.http_codes)
        self.expected_lable = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.expected_lable.setFont(font)
        self.expected_lable.setObjectName("expected_lable")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.expected_lable)
        self.expected = QtWidgets.QLineEdit(Dialog)
        self.expected.setMinimumSize(QtCore.QSize(0, 24))
        self.expected.setObjectName("expected")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.expected)
        self.notification = QtWidgets.QCheckBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notification.sizePolicy().hasHeightForWidth())
        self.notification.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.notification.setFont(font)
        self.notification.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.notification.setIconSize(QtCore.QSize(20, 20))
        self.notification.setObjectName("notification")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.notification)
        self.sound = QtWidgets.QCheckBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sound.sizePolicy().hasHeightForWidth())
        self.sound.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.sound.setFont(font)
        self.sound.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sound.setIconSize(QtCore.QSize(20, 20))
        self.sound.setObjectName("sound")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.sound)
        self.favourite = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.favourite.setFont(font)
        self.favourite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.favourite.setStyleSheet("QCheckBox {\n"
"    color: \"red\";\n"
"} \n"
"QCheckBox::indicator {\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(../media/star-off.png);\n"
"} \n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(../media/star-off-hover.png);\n"
"} \n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    image: url(../media/star-off-pressed.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(../media/star-on.png);\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"    image: url(../media/star-on-hover.png);\n"
"}\n"
"QCheckBox::indicator:checked:pressed {\n"
"    image: url(../media/star-on-pressed.png);\n"
"}")
        self.favourite.setObjectName("favourite")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.SpanningRole, self.favourite)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label)
        self.widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.save.setFont(font)
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.quit = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quit.sizePolicy().hasHeightForWidth())
        self.quit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.quit.setFont(font)
        self.quit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quit.setObjectName("quit")
        self.horizontalLayout.addWidget(self.quit)
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.SpanningRole, self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.http_method, self.http_headers)
        Dialog.setTabOrder(self.http_headers, self.http_body)
        Dialog.setTabOrder(self.http_body, self.http_proxy)
        Dialog.setTabOrder(self.http_proxy, self.https_proxy)
        Dialog.setTabOrder(self.https_proxy, self.http_codes)
        Dialog.setTabOrder(self.http_codes, self.expected)
        Dialog.setTabOrder(self.expected, self.notification)
        Dialog.setTabOrder(self.notification, self.sound)
        Dialog.setTabOrder(self.sound, self.save)
        Dialog.setTabOrder(self.save, self.quit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.header.setText(_translate("Dialog", "Settings - [SITENAME]"))
        self.http_method_label.setText(_translate("Dialog", "HTTP method"))
        self.http_headers_label.setText(_translate("Dialog", "HTTP headers"))
        self.http_body_label.setText(_translate("Dialog", "HTTP request body"))
        self.http_proxy_label.setText(_translate("Dialog", "Proxies HTTP"))
        self.https_proxy_label.setText(_translate("Dialog", "Proxies HTTPS"))
        self.http_codes_label.setText(_translate("Dialog", "HTTP expected codes (comma-separated)"))
        self.expected_lable.setText(_translate("Dialog", "Expected server response"))
        self.notification.setText(_translate("Dialog", "Send notification if server not responding"))
        self.sound.setText(_translate("Dialog", "Play sound if server not responding"))
        self.favourite.setText(_translate("Dialog", "Favourite"))
        self.label.setText(_translate("Dialog", "Icon"))
        self.save.setText(_translate("Dialog", "Save settings and quit"))
        self.quit.setText(_translate("Dialog", "Quit without saving"))

