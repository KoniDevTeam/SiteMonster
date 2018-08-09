from PyQt5 import QtGui


def set_wnd_icon(self, ico):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap('../media/' + ico), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.setWindowIcon(icon)
