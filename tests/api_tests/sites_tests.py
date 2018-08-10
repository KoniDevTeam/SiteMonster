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
