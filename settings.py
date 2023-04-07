import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))

PROFILES_DIR = os.path.join(BASE_DIR, 'profiles')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
