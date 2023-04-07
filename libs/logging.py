import logging as base_logging
from datetime import datetime


class AppLogHandler(base_logging.Handler):
    def __init__(self, log_text_field, *args, **kwargs):
        super(AppLogHandler, self).__init__(*args, **kwargs)
        self.log_text_field = log_text_field

    def emit(self, record):
        text = self.log_text_field.toPlainText().split('\n')
        text.append("[{}]: {}".format(datetime.now(), record.getMessage()))
        self.log_text_field.setText("\n".join(text[-1000:]))
        self.log_text_field.verticalScrollBar().setValue(self.log_text_field.verticalScrollBar().maximum())
