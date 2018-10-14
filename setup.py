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
