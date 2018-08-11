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
        Dialog.setMinimumSize(QtCore.QSize(640, 480))
        Dialog.setMaximumSize(QtCore.QSize(1920, 1080))
        self.hboxlayout = QtWidgets.QHBoxLayout(Dialog)
        self.hboxlayout.setSpacing(0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.menu_vert_ = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_vert_.sizePolicy().hasHeightForWidth())
        self.menu_vert_.setSizePolicy(sizePolicy)
        self.menu_vert_.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menu_vert_.setObjectName("menu_vert_")
        self.menu_vert = QtWidgets.QVBoxLayout(self.menu_vert_)
        self.menu_vert.setContentsMargins(0, 0, 0, -1)
        self.menu_vert.setSpacing(6)
        self.menu_vert.setObjectName("menu_vert")
        self.menu_btn = QtWidgets.QPushButton(self.menu_vert_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy)
        self.menu_btn.setMinimumSize(QtCore.QSize(24, 24))
        self.menu_btn.setMaximumSize(QtCore.QSize(32, 32))
        self.menu_btn.setSizeIncrement(QtCore.QSize(1, 1))
        self.menu_btn.setBaseSize(QtCore.QSize(24, 24))
        self.menu_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_btn.setToolTipDuration(1)
        self.menu_btn.setStyleSheet("QPushButton{\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"QPushButton[state=\"false\"]{\n"
"    border-image: url(../media/menu.png) 24px;\n"
"}\n"
"QPushButton[state=\"true\"]{\n"
"    border-image: url(../media/back.png) 24px;\n"
"}")
        self.menu_btn.setText("")
        self.menu_btn.setIconSize(QtCore.QSize(24, 24))
        self.menu_btn.setCheckable(False)
        self.menu_btn.setDefault(False)
        self.menu_btn.setFlat(True)
        self.menu_btn.setProperty("state", False)
        self.menu_btn.setObjectName("menu_btn")
        self.menu_vert.addWidget(self.menu_btn)
        self.fav_only_checkbox = QtWidgets.QCheckBox(self.menu_vert_)
        self.fav_only_checkbox.setStyleSheet("QCheckBox::indicator {\n"
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
        self.fav_only_checkbox.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../media/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fav_only_checkbox.setIcon(icon)
        self.fav_only_checkbox.setIconSize(QtCore.QSize(24, 24))
        self.fav_only_checkbox.setChecked(True)
        self.fav_only_checkbox.setObjectName("fav_only_checkbox")
        self.menu_vert.addWidget(self.fav_only_checkbox)
        self.fav_container_ = QtWidgets.QWidget(self.menu_vert_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fav_container_.sizePolicy().hasHeightForWidth())
        self.fav_container_.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.fav_container_.setFont(font)
        self.fav_container_.setObjectName("fav_container_")
        self.fav_container = QtWidgets.QVBoxLayout(self.fav_container_)
        self.fav_container.setContentsMargins(0, 0, 0, 0)
        self.fav_container.setSpacing(15)
        self.fav_container.setObjectName("fav_container")
        self.fav_btn_example = QtWidgets.QPushButton(self.fav_container_)
        self.fav_btn_example.setMaximumSize(QtCore.QSize(256, 32))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../media/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fav_btn_example.setIcon(icon1)
        self.fav_btn_example.setIconSize(QtCore.QSize(24, 24))
        self.fav_btn_example.setObjectName("fav_btn_example")
        self.fav_container.addWidget(self.fav_btn_example)
        self.menu_vert.addWidget(self.fav_container_)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menu_vert.addItem(spacerItem)
        self.plus_site = QtWidgets.QPushButton(self.menu_vert_)
        self.plus_site.setMinimumSize(QtCore.QSize(24, 24))
        self.plus_site.setMaximumSize(QtCore.QSize(32, 32))
        self.plus_site.setToolTipDuration(3500)
        self.plus_site.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../media/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plus_site.setIcon(icon2)
        self.plus_site.setIconSize(QtCore.QSize(24, 24))
        self.plus_site.setFlat(True)
        self.plus_site.setObjectName("plus_site")
        self.menu_vert.addWidget(self.plus_site)
        self.settings_btn = QtWidgets.QPushButton(self.menu_vert_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setMinimumSize(QtCore.QSize(24, 24))
        self.settings_btn.setMaximumSize(QtCore.QSize(32, 32))
        self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.settings_btn.setTabletTracking(False)
        self.settings_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.settings_btn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.settings_btn.setAcceptDrops(False)
        self.settings_btn.setToolTipDuration(1)
        self.settings_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../media/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon3)
        self.settings_btn.setIconSize(QtCore.QSize(24, 24))
        self.settings_btn.setFlat(True)
        self.settings_btn.setObjectName("settings_btn")
        self.menu_vert.addWidget(self.settings_btn)
        self.hboxlayout.addWidget(self.menu_vert_)
        self.container_ = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container_.sizePolicy().hasHeightForWidth())
        self.container_.setSizePolicy(sizePolicy)
        self.container_.setAccessibleName("")
        self.container_.setObjectName("container_")
        self.container = QtWidgets.QHBoxLayout(self.container_)
        self.container.setContentsMargins(-1, 0, -1, 0)
        self.container.setObjectName("container")
        self.line = QtWidgets.QFrame(self.container_)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.container.addWidget(self.line)
        self.content_ = QtWidgets.QWidget(self.container_)
        self.content_.setObjectName("content_")
        self.content = QtWidgets.QVBoxLayout(self.content_)
        self.content.setContentsMargins(1, 0, 1, 0)
        self.content.setObjectName("content")
        self.message_label = QtWidgets.QLabel(self.content_)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(20)
        self.message_label.setFont(font)
        self.message_label.setWordWrap(True)
        self.message_label.setObjectName("message_label")
        self.content.addWidget(self.message_label)
        self.description_ = QtWidgets.QWidget(self.content_)
        self.description_.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.description_.setFont(font)
        self.description_.setObjectName("description_")
        self.formLayout = QtWidgets.QFormLayout(self.description_)
        self.formLayout.setObjectName("formLayout")
        self.url_label = QtWidgets.QLabel(self.description_)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.url_label.setFont(font)
        self.url_label.setObjectName("url_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.url_label)
        self.url = QtWidgets.QLabel(self.description_)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.url.setFont(font)
        self.url.setObjectName("url")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.url)
        self.status_label = QtWidgets.QLabel(self.description_)
        self.status_label.setObjectName("status_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.status_label)
        self.status = QtWidgets.QLabel(self.description_)
        self.status.setStyleSheet("color: \"red\"")
        self.status.setObjectName("status")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.status)
        self.content.addWidget(self.description_)
        self.site_settings = QtWidgets.QPushButton(self.content_)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.site_settings.setFont(font)
        self.site_settings.setIcon(icon3)
        self.site_settings.setIconSize(QtCore.QSize(24, 24))
        self.site_settings.setObjectName("site_settings")
        self.content.addWidget(self.site_settings)
        self.add_site_btn = QtWidgets.QPushButton(self.content_)
        self.add_site_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_site_btn.sizePolicy().hasHeightForWidth())
        self.add_site_btn.setSizePolicy(sizePolicy)
        self.add_site_btn.setMinimumSize(QtCore.QSize(0, 32))
        self.add_site_btn.setMaximumSize(QtCore.QSize(16777214, 16777214))
        self.add_site_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.add_site_btn.setFont(font)
        self.add_site_btn.setObjectName("add_site_btn")
        self.content.addWidget(self.add_site_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.content.addItem(spacerItem1)
        self.delete_site = QtWidgets.QPushButton(self.content_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_site.sizePolicy().hasHeightForWidth())
        self.delete_site.setSizePolicy(sizePolicy)
        self.delete_site.setMinimumSize(QtCore.QSize(24, 24))
        self.delete_site.setMaximumSize(QtCore.QSize(32, 32))
        self.delete_site.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.delete_site.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../media/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_site.setIcon(icon4)
        self.delete_site.setIconSize(QtCore.QSize(24, 24))
        self.delete_site.setFlat(True)
        self.delete_site.setObjectName("delete_site")
        self.content.addWidget(self.delete_site)
        self.container.addWidget(self.content_)
        self.hboxlayout.addWidget(self.container_)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.menu_btn, self.fav_btn_example)
        Dialog.setTabOrder(self.fav_btn_example, self.add_site_btn)
        Dialog.setTabOrder(self.add_site_btn, self.settings_btn)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.menu_btn.setToolTip(_translate("Dialog", "Menu"))
        self.fav_btn_example.setText(_translate("Dialog", "Hello"))
        self.plus_site.setToolTip(_translate("Dialog", "add one more site"))
        self.settings_btn.setToolTip(_translate("Dialog", "Settings"))
        self.message_label.setText(_translate("Dialog", "To see your site status, please add it to site list."))
        self.url_label.setText(_translate("Dialog", "URL:"))
        self.url.setText(_translate("Dialog", "TextLabel"))
        self.status_label.setText(_translate("Dialog", "Status:"))
        self.status.setText(_translate("Dialog", "OMG"))
        self.site_settings.setText(_translate("Dialog", "Site settings"))
        self.add_site_btn.setText(_translate("Dialog", "Add site"))

