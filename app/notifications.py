import appinfo
import os

from api import osinfo


def send_windows_notification(message):
    if not osinfo.is_win10():
        raise OSError('Windows toast notifications can be sent only from Windows 10!')

    import win10toast

    toaster = win10toast.ToastNotifier()
    toaster.show_toast(appinfo.APP_NAME,
                       message,
                       icon_path=appinfo.APP_ICON,
                       duration=5,
                       threaded=True)


def send_linux_notification(message):
    if not osinfo.is_linux():
        raise OSError('Linux libnotify notifications can be sent only from linux-based OS!')
    if appinfo.APP_ICON is not None:
        os.system('notify-send "{}" "{}" -i {}'.format(appinfo.APP_NAME, message, os.path.abspath(appinfo.APP_ICON)))
    else:
        os.system('notify-send "{}" "{}"'.format(appinfo.APP_NAME, message))
