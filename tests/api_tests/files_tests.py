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

from api import files

files_ = {}


class PatchedStream:

    mode = ''
    closed = False
    file = ''

    def __init__(self, filename, mode):
        self.mode = mode
        self.file = filename

    def read(self):
        try:
            if self.closed:
                raise PermissionError('Reading from closed file')
            return files_[self.file]
        except KeyError:
            raise FileNotFoundError('[Errno 2] No such file or directory')

    def write(self, file):
        global files_
        if self.closed:
            raise PermissionError('Writing to closed file')
        if self.mode != 'w' and self.mode != 'a':
            raise PermissionError('Writing to read-only file')
        files_[self.file] = file

    def close(self):
        self.closed = True


def open_patched(filename, mode, buffering=None, encoding=None, errors=None, newline=None, closefd=True):
    return PatchedStream(filename, mode)


class FilesTests(unittest.TestCase):
    @patch('builtins.open', open_patched)
    def test_read_write_empty(self):
        object_ = {}
        files.save(object_, "test666")
        self.assertEqual(files.read("test666"), object_)

    @patch('builtins.open', open_patched)
    def test_read_write_dict(self):
        object_ = {"Hey": 823, "test2": [23, 'dd', {'t': 'w', 'w': []}]}
        files.save(object_, "test666")
        self.assertEqual(files.read("test666"), object_)

    @patch('builtins.open', open_patched)
    def test_read_from_not_exist(self):
        self.assertRaises(FileNotFoundError, files.read, "test267462783627834")


if __name__ == '__main__':
    unittest.main()
