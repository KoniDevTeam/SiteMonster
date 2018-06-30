"""Actions with websites."""

import requests


def check(site: dict) -> bool:
    """Check if site is available."""

    settings = site['settings']

    success = True
    r = None

    try:
        r = requests.request(settings['method'], site['url'], headers=settings['headers'], data=settings['body'], proxies=settings['proxy'])
    except Exception:
        success = False

    return success and ((settings['expected_code'] is None and (200 <= r.status_code < 300)) or (r.status_code in settings['expected_code'])) and (settings['expected_answer'] is None or (r.text == settings['expected_answer']))
