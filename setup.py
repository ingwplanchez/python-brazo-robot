## python setup.py py2exe
from distutils.core import setup
import py2exe
setup(scripts=['Brazo5GDLGUI_COM5.py'],
      windows=['Brazo5GDLGUI_COM5.py'],
      options ={"py2exe": {"bundle_files": 1}},
      zipfile=None)
