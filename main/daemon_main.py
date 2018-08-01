import time

import api.sites as sites
import app.site as site
import app.notifications as notify

if __name__ == "__main__":
    while True:
        sites_dict = site.get_sites_list()
        for i, j in sites_dict.items():
            if not sites.check(j):
                if j['settings']['fail_actions']['send_notification']:
                    notify.send_notification('Site %s is down!!!' % i)
                if j['settings']['fail_actions']['play_sound']:
                    notify.play_sound()
                time.sleep(30)
        time.sleep(1)
