"""
Usage:
    python setup.py py2app

"""

from setuptools import setup

APP = ['Main.py']
#DATA_FILES = [('', ['images']), ('', ['audio'])]
#OPTIONS = {'iconfile':'ship.icns',}

setup(
    app = APP,
  #  data_files = DATA_FILES,
 #   options = {'py2app': OPTIONS},
    setup_requires = ['py2app'],
)
