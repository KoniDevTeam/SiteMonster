"""Logging methods"""

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


import logging
import platform

from api import files


def init_log(sess_name):
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.DEBUG)
    logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                        level=logging.DEBUG, filename=files.get_data_folder() + 'latest-' + sess_name + '.log')

def log_pc_info():
    logging.info("Machine - " + platform.machine())
    logging.info("System - " + platform.system())
    logging.info("System release - " + platform.release())
    logging.info("System version - " + platform.version())
    logging.info("CPU - " + platform.processor())
    logging.info("uname - " + str(platform.uname()))
