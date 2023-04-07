import configparser
import os
import pathlib
from subprocess import call

from paver import easy

config = configparser.ConfigParser()
config.read('config.ini')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@easy.task
def build_ui():
    ui_path = os.path.join(BASE_DIR, 'QT')
    files = list(easy.path(ui_path).walkfiles('*.ui'))
    pyside_uic_path = os.path.join(BASE_DIR, config['build']['PySideUICScriptPath'])
    for file in files:
        py_file = os.path.join(BASE_DIR, 'ui', file.abspath().replace(ui_path, '').strip('/').strip('\\').replace('.ui', '.py'))
        try:
            pathlib.Path(os.path.dirname(py_file)).mkdir(parents=True)
        except FileExistsError:
            pass
        with open(py_file, 'w') as f:
            easy.info("Build ui file '{}' to '{}'".format(file.relpath(), py_file))
            call([pyside_uic_path, '--from-imports', file.relpath()], stdout=f)
