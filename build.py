import sys

from cx_Freeze import Executable, setup

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

build_exe_options = {
    "include_msvcr": True,
    "path": sys.path,
    "excludes": [],
    "packages": [
        'pynput',
        'six',
        'keyboard'
    ],
    'include_files': [],
    # "create_shared_zip": False,
    # "append_script_to_exe": True
}

setup(
    name='RClicker2',
    version='0.1',
    description="",
    options={"build_exe": build_exe_options},
    executables=[
        Executable("main.py",
               base=base,
               # compress=True,
               # copyDependentFiles=True,
               # appendScriptToExe=True,
               # appendScriptToLibrary=False,
           )
    ]
)
