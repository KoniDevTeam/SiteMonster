"""Edit sites list."""

import os

from api import files

SITES_LIST_FILE = 'siteList.json'


def get_sites_list() -> dict:
    """Read sites list from json."""

    if os.path.exists(files.get_data_folder() + SITES_LIST_FILE):
        return files.read(SITES_LIST_FILE)
    else:
        return dict()


def save_sites_list(sites_obj: object):
    """Save sites list to file."""

    files.save(sites_obj, SITES_LIST_FILE)


def add(name: str, url: str, settings: dict):
    """Add url to sites list.

    Generate settings dictionary by `build_settings` method.

    NameError - if than name already exists.

    """

    sites = get_sites_list()

    if name in sites.keys():
        return NameError('Name already exists.')

    sites[name] = {'url': url, 'settings': settings}
    save_sites_list(sites)


def delete(name: str):
    """Remove url from sites list.

    NameError - if than name not exists.

    """

    sites = get_sites_list()

    if name not in sites.keys():
        return NameError('Name not exists.')

    del sites[name]
    save_sites_list(sites)


def rename(old_name: str, new_name: str):
    """Rename url in sites list.

    NameError - if new name already exists or old name not exists.

    """

    sites = get_sites_list()

    if old_name not in sites.keys():
        return NameError('Old name not exists.')
    if new_name in sites.keys():
        return NameError('New name already exists.')

    sites[new_name] = sites.pop(old_name)
    save_sites_list(sites)


def change_settings(name: str, settings: dict):
    """Change url's settings.

    Generate settings dictionary by `build_settings` method.

    NameError - if than name not exists.

    """

    sites = get_sites_list()

    if name not in sites.keys():
        return NameError('Name not exists.')

    sites[name]["settings"] = settings
    save_sites_list(sites)


def get_list() -> list:
    """Get list of sites' names"""

    return list(get_sites_list().keys())


def build_settings(method='GET', headers=None, body='', proxy=None, expected_code=None, expected_answer=None,
                   fail_actions=None) -> dict:
    """Generate settings dictionary.

    method - string, HTTP method which with send request to check website availability.
    headers - dictionary or NoneType, HTTP request headers.
    body - string, HTTP request body.
    proxy - dictionary or NoneType, proxies which will be used to send HTTP request.
    expected_code - list of int or NoneType, expected HTTP status code (More info: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes), if None - accept any from 200 to 299.
    expected_answer - string or NoneType, expected response body, if None - accept any.
    fail_actions - dict or NoneType, what do if site is unavailable, generate with `build_fail_actions` method.

    """

    if fail_actions is None:
        fail_actions = build_fail_actions()

    return {'method': method, 'headers': headers, 'body': body, 'proxy': proxy, 'expected_code': expected_code,
            'expected_answer': expected_answer, 'fail_actions': fail_actions}


def build_fail_actions(send_notification=True, play_sound=True) -> dict:
    """Generate fail actions dictionary.

    send_notifications - bool, if True send push notifications to PC (`send_notification` method in `app/notifications.py`).
    play_sound - bool, if True plays alarm sound on your PC to PC (`play_sound` method in `app/notifications.py`).

    """

    return {'send_notification': send_notification, 'play_sound': play_sound}
