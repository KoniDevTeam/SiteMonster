import appinfo
import plyer


def send_notification(message, title):
    plyer.notification.notify(message=message, app_name=appinfo.APP_NAME, app_icon=appinfo.APP_ICON, title=title)
