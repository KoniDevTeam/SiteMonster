"""Get some info about user's OS."""

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

import platform


def is_win10() -> bool:
    is_win_10 = is_win() and '10' in platform.release()

    return is_win_10


def is_win() -> bool:
    is_win_ = 'Windows' in platform.system()

    return is_win_


def is_mac_os() -> bool:
    is_mac = 'Darwin' in platform.system()

    return is_mac


def is_linux() -> bool:
    is_linux_ = 'Linux' in platform.system()

    return is_linux_
