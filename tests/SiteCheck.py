import unittest

from api import sites
from app import site


class CheckTest(unittest.TestCase):
    def test_success(self):
        self.assertTrue(sites.check({'url': 'https://google.com/', 'settings': site.build_settings()}))

    def test_error(self):
        self.assertTrue(sites.check({'url': 'http://google.com/ahshhs', 'settings': site.build_settings(expected_code=[404])}))

    def test_no_site(self):
        self.assertFalse(sites.check({'url': 'http://wgdgdggdg.com/', 'settings': site.build_settings()}))


if __name__ == '__main__':
    unittest.main()
