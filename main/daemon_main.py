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

import time
from logapi import logging_daemon as logging
import os

import app.notifications as notify
from app import site
from api import sites
import appinfo


def save_pid():
    f = open(appinfo.PID_FILE, 'w')
    f.write(str(os.getpid()))
    f.close()


def check_site(name: str, site_data: dict):
    if not sites.check(site_data):
        fail_actions = site_data['settings']['fail_actions']
        if fail_actions['send_notification']:
            logging.warning('Site %s is down!!!' % name)
            notify.send_notification('Site %s is down!!!' % name)
        if fail_actions['play_sound']:
            notify.play_sound()
        time.sleep(30)


if __name__ == '__main__':
    save_pid()
    while True:
        sites_dict = site.get_sites_dict()
        for i, j in sites_dict.items():
            logging.info("Checking " + i)
            check_site(i, j)
        time.sleep(1)
