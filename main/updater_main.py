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
import logging

from PyQt5.QtWidgets import QApplication

from gui.update_tool import UpdateToolWindow
from app import logger

if __name__ == '__main__':
    logger.init_log('updater')
    logger.log_pc_info()
    app = QApplication(sys.argv)
    updater_window = UpdateToolWindow(app.primaryScreen().size())

    logging.info('Starting updater')

    app.exec_()
