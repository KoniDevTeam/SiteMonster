import time
import logging

import api.sites as sites
import app.site as site
import app.notifications as notify
from app import logger

if __name__ == '__main__':
    logger.init_log('daemon')
    logger.log_pc_info()
    while True:
        sites_dict = site.get_sites_dict()
        for i, j in sites_dict.items():
            if not sites.check(j):
                if j['settings']['fail_actions']['send_notification']:
                    logging.warning('Site %s is down!!!' % i)
                    notify.send_notification('Site %s is down!!!' % i)
                if j['settings']['fail_actions']['play_sound']:
                    notify.play_sound()
                time.sleep(30)
        time.sleep(1)
