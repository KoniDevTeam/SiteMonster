"""Send notification to user."""

import wave
import os
import sys
import platform

import pyaudio

from PyQt5 import Qt

import appinfo
import api.files

from api import osinfo


def send_old_windows_notification(message: str):
    """Show tray popup on old windows."""

    app = Qt.QApplication(sys.argv)
    systemtray_icon = None
    if appinfo.APP_ICON is not None and open(appinfo.APP_ICON):
        systemtray_icon = Qt.QSystemTrayIcon(Qt.QIcon(appinfo.APP_ICON))
    else:
        systemtray_icon = Qt.QSystemTrayIcon()
    systemtray_icon.show()
    systemtray_icon.showMessage(appinfo.APP_NAME, message)


def send_windows_notification(message: str):
    """Send windows 10 toast notification."""

    if not osinfo.is_win10():
        raise OSError('Windows toast notifications can be sent only from Windows 10!')

    import win10toast

    toaster = win10toast.ToastNotifier()
    toaster.show_toast(appinfo.APP_NAME,
                       message,
                       icon_path=appinfo.APP_ICON,
                       duration=5,
                       threaded=True)


def send_linux_notification(message: str):
    """Send linux libnotify notification."""

    if not osinfo.is_linux():
        raise OSError('Linux libnotify notifications can be sent only from linux-based OS!')
    if appinfo.APP_ICON is not None:
        os.system('notify-send "{}" "{}" -i {}'.format(appinfo.APP_NAME, message, os.path.abspath(appinfo.APP_ICON)))
    else:
        os.system('notify-send "{}" "{}"'.format(appinfo.APP_NAME, message))


def send_mac_os_notification(message: str):
    """Send macOS push notification."""

    if not osinfo.is_mac_os():
        raise OSError('MacOS notifications can be sent only from MacOS!')
    if appinfo.APP_ICON is not None:
        os.system('terminal-notifier -title "{}" -subtitle "" -message "{}" -appIcon "{}"'.format(appinfo.APP_NAME,
                                                                                                  message,
                                                                                                  appinfo.APP_ICON))
    else:
        os.system('terminal-notifier -title "{}" -subtitle "" -message "{}"'.format(appinfo.APP_NAME, message))


def send_notification(message):
    """Send push notification to your PC."""

    if osinfo.is_win10():
        send_windows_notification(message)
    elif osinfo.is_win():
        send_old_windows_notification(message)
    elif osinfo.is_linux():
        send_linux_notification(message)
    elif osinfo.is_mac_os():
        send_mac_os_notification(message)
    else:
        raise OSError("Unknown OS: " + platform.system())


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
