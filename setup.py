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
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['atexit', 'api', 'app', 'gui', 'logapi', 'gui.ui', 'idna.idnadata', 'appdirs', 'packaging.version',
                     'packaging', 'packaging.specifiers', 'packaging.requirements', 'daemon'],
        'optimize': 1
    }
}

executables = [
    Executable('main/main.py', base="Win32GUI", icon='media/logo.ico'),
    Executable('main/updater.py', base="Win32GUI", icon='media/logo.ico'),
    Executable('main/daemon.py', base="Win32GUI", icon='media/logo.ico')
]

setup(name='Site Monster',
      version='1.0.1',
      description='Site Monster',
      options=options,
      executables=executables
      )
