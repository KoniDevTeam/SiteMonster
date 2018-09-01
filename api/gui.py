from PyQt5 import QtGui

from api import files


def set_wnd_icon(self, ico):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(files.get_media_folder_path() + ico), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.setWindowIcon(icon)