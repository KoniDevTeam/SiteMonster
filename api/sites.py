"""Actions with websites."""

# Copyright (C) 2018 Koni Dev Team, All Rights Reserved
# https://github.com/KoniDevTeam/SiteMonster/
#
# This file is part of Site Monster.
#
# Site Monster is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Site Monster is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Site Monster.  If not, see <https://www.gnu.org/licenses/>.

from logapi import logging_daemon as logging

import requests


def check(site: dict) -> bool:
    """Check if site is available."""

    logging.info('Checking ' + site['url'])

    settings = site['settings']

    success = True
    r = None

    url = site['url']

    try:
        r = requests.request(settings['method'], url, headers=settings['headers'], data=settings['body'],
                             proxies=settings['proxy'])
    except Exception:
        success = False

    if not success:
        logging.info("Can't send request to " + url)
        site_ = site.copy()
        if '://' not in url:
            site_['url'] = 'http://' + url
            c = check(site_)
            if not c:
                site_['url'] = 'https://' + url
                c = check(site_)
            return c
        return False

    if not is_status_code_good(settings['expected_code'], r.status_code):
        logging.info("Invalid response's status code: expected " + str(settings['expected_code']) + ', got ' + str(
            r.status_code) + ' on ' + url)
        return False

    if not is_answer_good(settings['expected_answer'], r.text):
        logging.info("Invalid server's response: expected" + str(settings['expected_answer']) + ', got ' + r.text + ' on ' + url)
        return False

    return True


def is_status_code_good(expected_codes: list, status_code: int) -> bool:
    """Check if status_code is in expected_codes

    If expected_code is None, checks if status_code is from 200 to 299
    """
    return (expected_codes is None and (200 <= status_code < 300)) or (status_code in expected_codes)


def is_answer_good(expected_answer: str, response: str) -> bool:
    """Check if anser is in expected_codes

    If expected_code is None, checks if status_code is from 200 to 299
    """

    is_accepting_any_answer = expected_answer is None or expected_answer is ''
    return is_accepting_any_answer or response == expected_answer
