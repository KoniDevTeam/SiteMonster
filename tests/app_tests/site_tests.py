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

from app import site

file = ''
obj = {}


def read_from_disk(filename):
    if file == filename:
        return obj
    else:
        return {}


def write_to_disk(obj_, filename):
    global obj, file
    obj = obj_
    file = filename


class SiteTests(unittest.TestCase):
    @patch('api.files.read', read_from_disk)
    @patch('api.files.save', write_to_disk)
    def test_get_sites_dict(self):  # Just check there aren't any errors
        site.get_sites_dict()
        site.get_list()

    @patch('api.files.read', read_from_disk)
    @patch('api.files.save', write_to_disk)
    def test_add_and_delete_website(self):  # Just check there aren't any errors
        site.add("New", "https://test.com/", site.build_settings())
        site.delete("New")

    @patch('api.files.read', read_from_disk)
    @patch('api.files.save', write_to_disk)
    def test_add_and_delete_website_favourite(self):  # Just check there aren't any errors
        site.add("New", "https://test.com/", site.build_settings(), True)
        site.delete("New")

    @patch('api.files.read', read_from_disk)
    @patch('api.files.save', write_to_disk)
    def test_add_and_double_delete_website(self):
        site.add("New", "https://test.com/", site.build_settings())
        site.delete("New")
        self.assertRaises(NameError, site.delete, "New")

    @patch('api.files.read', read_from_disk)
    @patch('api.files.save', write_to_disk)
    def test_double_add_and_delete_website(self):
        site.add("New", "https://test.com/", site.build_settings())
        self.assertRaises(NameError, site.add, "New", "https://test.com/", site.build_settings())
        site.delete("New")

    @patch('api.files.read', read_from_disk)
    @patch('api.files.save', write_to_disk)
    def test_create_rename_and_delete(self):  # Just check there aren't any errors
        site.add("New", "https://test.com/", site.build_settings())
        site.rename("New", "New2")
        site.delete("New2")

    @patch('api.files.read', read_from_disk)
    @patch('api.files.save', write_to_disk)
    def test_create_rename_to_same_name_and_delete(self):
        site.add("New", "https://test.com/", site.build_settings())
        self.assertRaises(NameError, site.rename, "New", "New")
        site.delete("New")

    @patch('api.files.read', read_from_disk)
    @patch('api.files.save', write_to_disk)
    def rename_not_exists(self):
        self.assertRaises(NameError, "New", "New2")

    @patch('api.files.read', read_from_disk)
    @patch('api.files.save', write_to_disk)
    def test_create_change_setting_and_delete(self):  # Just check there aren't any errors
        site.add("New", "https://test.com/", site.build_settings())
        site.change_settings("New", site.build_settings(
            "POST",
            None,
            '{}',
            None,
            [204, 205],
            'Just test',
            site.build_fail_actions(False, False)
        ))
        site.delete("New")

    @patch('api.files.read', read_from_disk)
    @patch('api.files.save', write_to_disk)
    def test_change_setting_site_not_exists(self):
        self.assertRaises(NameError, site.change_settings, "New", site.build_settings())


if __name__ == '__main__':
    unittest.main()
