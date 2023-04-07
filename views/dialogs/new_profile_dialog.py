from PySide6.QtWidgets import QDialog

from ui.dialogs.NewProfileDialog import Ui_Dialog


class NewProfileDialog(Ui_Dialog):
    def __init__(self, parent=None):
        self.dialog = QDialog(parent)
        self.setupUi(self.dialog)

    def setupUi(self, dialog):
        super(NewProfileDialog, self).setupUi(dialog)

    def get_profile_name(self):
        return self.profileName.text()

    def exec_(self, *args, **kwargs):
        return self.dialog.exec()
