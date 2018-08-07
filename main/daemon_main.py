import time
import logging
import os

import api.sites as sites
import app.site as site
import app.notifications as notify
from app import logger


PID_FILE = 'daemon_pid.tmp'


def save_pid():
    f = open(PID_FILE, 'w')
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
    logger.init_log('daemon')
    logger.log_pc_info()
    while True:
        sites_dict = site.get_sites_dict()
        for i, j in sites_dict.items():
            logging.info("Checking " + i)
            check_site(i, j)
        time.sleep(1)
