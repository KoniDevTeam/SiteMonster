import configparser

from api import osinfo

lang = "EN"


def init_locale():
    global lang

    if osinfo.is_win():
        import locale
        import ctypes

        windll = ctypes.windll.kernel32
        lang_ = locale.windows_locale[windll.GetUserDefaultUILanguage()]

        if "US" in lang_:
            lang = "US"
        elif "ru" in lang_:
            lang = "RU"
        elif "uk" in lang_:
            lang = "UA"
    else:
        pass  # TODO lang detection on linux & macOS
