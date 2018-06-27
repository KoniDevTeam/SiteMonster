from api import osinfo
import appinfo


def send_windows_notification(message):
    if not osinfo.is_win10():
        raise OSError("Windows toast notifications can be sent only from Windows 10!")
    import win10toast
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(appinfo.APP_NAME,
                       message,
                       icon_path=appinfo.APP_ICON,
                       duration=5,
                       threaded=True)