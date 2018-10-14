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

import sys

from pyloges.logger import Logger
from pyloges.classes.config import Config
from pyloges.handlers.file import FileHandler

from api import files

if hasattr(sys, 'frozen'):
    logger = Logger(Config(print_to_std=False))
else:
    logger = Logger(Config())

logger.config.add_handler(FileHandler(files.get_and_create_data_folder() + "app-latest.log"))


def info(msg):
    logger.i(msg)


def debug(msg):
    logger.d(msg)


def warning(msg):
    logger.w(msg)


def error(msg):
    logger.e(msg)


def critical(msg):
    logger.f(msg)
