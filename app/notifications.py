"""Send notification to user."""

import wave
import os
import sys

import pyaudio

from PyQt5 import Qt

import appinfo

from api import osinfo


def send_qt_notification(message: str):
    """Send qt notification."""

    app = Qt.QApplication(sys.argv)
    systemtray_icon = None
    if appinfo.APP_ICON is not None:
        systemtray_icon = Qt.QSystemTrayIcon(Qt.QIcon(appinfo.APP_ICON))
    else:
        systemtray_icon = Qt.QSystemTrayIcon()
    systemtray_icon.show()
    systemtray_icon.showMessage(appinfo.APP_NAME, message)


def send_mac_os_notification(message: str):
    """Send macOS push notification."""

    if not osinfo.is_mac_os():
        raise OSError('MacOS notifications can be sent only from MacOS!')
    if appinfo.APP_ICON is not None:
        os.system('terminal-notifier -title "{}" -subtitle "" -message "{}" -appIcon "{}"'.format(appinfo.APP_NAME, message, appinfo.APP_ICON))
    else:
        os.system('terminal-notifier -title "{}" -subtitle "" -message "{}"'.format(appinfo.APP_NAME, message))


def send_notification(message):
    """Send push notification to your PC."""

    if osinfo.is_mac_os():
        send_mac_os_notification(message)
    else:
        send_qt_notification(message)


def play_sound():
    """Plays alarm on user's PC"""
    chunk = 1024

    f = wave.open(r"../media/alarm.wav", "rb")
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()
