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
