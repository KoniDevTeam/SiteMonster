import unittest
from unittest.mock import patch

from requests.models import Response

from api import sites
from app import site


def request(method, url, **kwargs):
    response = Response()
    if url == 'https://google.com/':
        response._content = b'<html>Google!</html>'
        response.status_code = 200
    elif url == 'http://google.com/ahshhs':
        response._content = b'<html>Google 404!</html>'
        response.status_code = 404
    else:
        raise ConnectionError("Can't send request!")
    return response


class CheckTest(unittest.TestCase):
    @patch('requests.request', request)
    def test_success(self):
        self.assertTrue(sites.check({'url': 'https://google.com/', 'settings': site.build_settings()}))

    @patch('requests.request', request)
    def test_error(self):
        self.assertTrue(sites.check({'url': 'http://google.com/ahshhs', 'settings': site.build_settings(expected_code=[404])}))

    @patch('requests.request', request)
    def test_no_site(self):
        self.assertFalse(sites.check({'url': 'http://wgdgdggdg.com/', 'settings': site.build_settings()}))


if __name__ == '__main__':
    unittest.main()
