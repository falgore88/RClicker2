import logging
import sys

import qdarkstyle
from PySide6.QtWidgets import QApplication
from pathlib import Path
import settings
from libs.logging import AppLogHandler

from views.main_window import MainWindow

if __name__ == '__main__':
    logs_path = Path(settings.LOGS_DIR)
    logs_path.mkdir(parents=True, exist_ok=True)

    profiles_path = Path(settings.PROFILES_DIR)
    profiles_path.mkdir(parents=True, exist_ok=True)

    app = QApplication()

    main_window = MainWindow()

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    app_handler = AppLogHandler(main_window.logTextField)
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    app_handler.setFormatter(logFormatter)
    root_logger.addHandler(app_handler)

    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    main_window.show()
    sys.exit(app.exec())
