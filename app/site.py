"""Edit sites list."""

from api import files

SITES_LIST_FILE = 'siteList.json'


def get_sites_list() -> dict:
    """Read sites list from json."""

    return files.read(SITES_LIST_FILE)


def save_sites_list(sites_obj):
    """Save sites list to file."""

    files.save(sites_obj, SITES_LIST_FILE)


def add(name, url, settings):
    """Add url to sites list.

    Generate settings dictionary by `build_settings` method.

    NameError - if than name already exists.

    """

    sites = get_sites_list()

    if name in sites.keys():
        return NameError("Name already exists.")

    sites[name] = {"url": url, "settings": settings}
    save_sites_list(sites)


def delete(name):
    """Remove url from sites list.

    NameError - if than name not exists.

    """

    sites = get_sites_list()

    if name not in sites.keys():
        return NameError("Name not exists.")

    del sites[name]
    save_sites_list(sites)


def rename(old_name, new_name):
    """Rename url in sites list.

    NameError - if new name already exists or old name not exists.

    """

    sites = get_sites_list()

    if old_name not in sites.keys():
        return NameError("Old name not Oldexists.")
    if new_name in sites.keys():
        return NameError("New name already exists.")

    sites[new_name] = sites.pop(old_name)
    save_sites_list(sites)


def change_settings(name, settings):
    """Change url's settings.

    Generate settings dictionary by `build_settings` method.

    NameError - if than name not exists.

    """

    sites = get_sites_list()

    if name not in sites.keys():
        return NameError("Name not exists.")

    sites[name]["settings"] = settings
    save_sites_list(sites)


def get_list() -> list:
    """Get list of sites' names"""

    return list(get_sites_list().keys())


def build_settings(method='GET', headers=None, body='', proxy=None, expected_code=200, expected_answer='',
                   fail_actions=None) -> dict:
    """Generate settings dictionary.

    method - string, HTTP method which with send request to check website availability.
    headers - dictionary or NoneType, HTTP request headers.
    body - string, HTTP request body.
    proxy - dictionary or NoneType, proxies which will be used to send HTTP request.
    expected_code - int, expected HTTP status code (More info: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).
    expected_answer - string, expected response body.
    fail_actions - dict or NoneType, what do if site is unavailable, generate with `build_fail_actions` method.

    """

    return {"method": method, "headers": headers, "body": body, "proxy": proxy, "expected_code": expected_code,
            "expected_answer": expected_answer, "fail_actions": fail_actions}


def build_fail_actions(send_notification=True, play_sound=True) -> dict:
    """Generate fail actions dictionary.

    send_notifications - bool, if True send push notifications to PC (`send_notification` method in `app/notifications.py`).
    play_sound - bool, if True plays alarm sound on your PC to PC (`play_sound` method in `app/notifications.py`).

    """

    return {"send_notification": send_notification, "play_sound": play_sound}
