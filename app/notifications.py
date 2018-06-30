"""Send notification to user."""

import appinfo
import wave
import os

import pyaudio

from api import osinfo


def _send_windows_notification(message):
    if not osinfo.is_win10():
        raise OSError('Windows toast notifications can be sent only from Windows 10!')

    import win10toast

    toaster = win10toast.ToastNotifier()
    toaster.show_toast(appinfo.APP_NAME,
                       message,
                       icon_path=appinfo.APP_ICON,
                       duration=5,
                       threaded=True)


def _send_linux_notification(message):
    if not osinfo.is_linux():
        raise OSError('Linux libnotify notifications can be sent only from linux-based OS!')
    if appinfo.APP_ICON is not None:
        os.system('notify-send "{}" "{}" -i {}'.format(appinfo.APP_NAME, message, os.path.abspath(appinfo.APP_ICON)))
    else:
        os.system('notify-send "{}" "{}"'.format(appinfo.APP_NAME, message))


def _send_mac_os_notification(message):
    if not osinfo.is_mac_os():
        raise OSError('MacOS notifications can be sent only from MacOS!')
    if appinfo.APP_ICON is not None:
        os.system('terminal-notifier -title "{}" -subtitle "" -message "{}" -appIcon "{}"'.format(appinfo.APP_NAME, message, appinfo.APP_ICON))
    else:
        os.system('terminal-notifier -title "{}" -subtitle "" -message "{}"'.format(appinfo.APP_NAME, message))



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
