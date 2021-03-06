"""Send notification to user."""

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

import wave
import os
import sys
import platform
from logapi import logging

import pyaudio
from PyQt5 import Qt

import appinfo
from api import osinfo, files


def send_windows_notification(message: str):
    """Send windows 10 toast notification."""

    logging.debug('Sending windows 10 toast notification')

    if not osinfo.is_win():
        logging.error('Trying to send win10 notification not from win10!')
        raise OSError('Windows toast notifications can be sent only from Windows 10!')

    import win10toast

    toaster = win10toast.ToastNotifier()
    toaster.show_toast(appinfo.APP_NAME,
                       message,
                       icon_path=appinfo.APP_ICON,
                       duration=5,
                       threaded=True)


def send_linux_notification(message: str):
    """Send linux libnotify notification."""

    logging.debug('Sending linux libnotify notification')

    if not osinfo.is_linux():
        logging.error('Trying to send linux notification not from linux!')
        raise OSError('Linux libnotify notifications can be sent only from linux-based OS!')
    if appinfo.APP_ICON is not None:
        os.system('notify-send "{}" "{}" --icon="{}" --expire-time=30000'.format(appinfo.APP_NAME, message, os.path.abspath(appinfo.APP_ICON)))
    else:
        os.system('notify-send "{}" "{}" --expire-time=30000'.format(appinfo.APP_NAME, message))


def send_mac_os_notification(message: str):
    """Send macOS push notification."""

    logging.debug('Sending macos push notification')

    if not osinfo.is_mac_os():
        logging.error('Trying to send macOS notification not from macOS!')
        raise OSError('MacOS notifications can be sent only from MacOS!')
    if appinfo.APP_ICON is not None:
        os.system('terminal-notifier -title "{}" -subtitle "" -message "{}" -appIcon "{}"'.format(appinfo.APP_NAME,
                                                                                                  message,
                                                                                                  appinfo.APP_ICON))
    else:
        os.system('terminal-notifier -title "{}" -subtitle "" -message "{}"'.format(appinfo.APP_NAME, message))


def send_notification(message):
    """Send push notification to your PC."""

    logging.info('Sending notification')

    if osinfo.is_win():
        send_windows_notification(message)
    elif osinfo.is_linux():
        send_linux_notification(message)
    elif osinfo.is_mac_os():
        send_mac_os_notification(message)
    else:
        raise OSError("Unknown OS: " + platform.system())


def play_sound():
    """Plays alarm on user's PC"""
    chunk = 1024

    logging.info('Playing sound')

    f = wave.open(files.get_media_folder_path() + r"/alarm.wav", "rb")
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()
