import logging

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QTableWidgetItem, QPushButton, QDialog, QMenu, QHeaderView

from core.profile import Profile
from core.rotation import Rotation
from ui.mainwindow import Ui_MainWindow
from views.dialogs.new_profile_dialog import NewProfileDialog
from views.dialogs.rotation_battle_dialog import RotationBattleDialog
from views.dialogs.rotation_heal_dialog import RotationHealDialog


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.profile_list = []

    def setupUi(self, main_window):
        super(MainWindow, self).setupUi(main_window)
        self.update_profile_list(init=True)

        self.rotationTable.customContextMenuRequested.connect(self.open_menu)

        self.rotationTable.doubleClicked.connect(self.on_select_rotation)

        header = self.rotationTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.addProfileButton.clicked.connect(self.on_add_new_profile)
        self.profileComboBox.currentIndexChanged.connect(self.on_change_profile)

    def on_change_profile(self, index):
        print(index)
        self.update_rotation_list(index)
        logging.info("Смена профайла: {}".format(self.get_current_profile()))

    def open_menu(self, position, *args, **kwargs):
        if self.get_current_profile():
            row = self.rotationTable.rowAt(position.y())
            menu = QMenu()
            create_rotation_action = menu.addAction("Добавить боевую ротацию")
            create_rotation_action.triggered.connect(self.on_create_new_rotation(Rotation.TYPE_BATTLE))

            create_rotation_action = menu.addAction("Добавить хил ротацию")
            create_rotation_action.triggered.connect(self.on_create_new_rotation(Rotation.TYPE_HEAL))

            if row != -1:
                remove_rotation_action = menu.addAction("Удалить ротацию")
                remove_rotation_action.triggered.connect(self.on_remove_rotation(row))
            menu.exec_(self.rotationTable.mapToGlobal(position))

    def on_create_new_rotation(self, type):
        def wrap():
            profile = self.get_current_profile()
            if type == Rotation.TYPE_BATTLE:
                dialog = RotationBattleDialog(profile, self)
            else:
                dialog = RotationHealDialog(profile, self)
            dialog.exec_()
            profile.save()
            self.update_rotation_list()

        return wrap

    def on_select_rotation(self, index, *args, **kwargs):
        profile = self.get_current_profile()
        rotation = profile.rotations[index.row()]
        rotation.stop()
        profile = self.get_current_profile()
        if rotation.type == Rotation.TYPE_BATTLE:
            dialog = RotationBattleDialog(profile, self, rotation)
        else:
            dialog = RotationHealDialog(profile, self, rotation)
        logging.info("Открытие ротации: {}".format(rotation.name))
        dialog.exec_()
        profile.save()
        self.update_rotation_list()

    def update_profile_list(self, new_profile=None, init=False):
        self.profile_list = Profile.load_profiles()
        self.profileComboBox.setDisabled(True)
        self.profileComboBox.clear()
        if self.profile_list:
            for index, profile in enumerate(self.profile_list):
                self.profileComboBox.addItem(profile.name, profile)
                if new_profile and new_profile.name == profile.name:
                    self.profileComboBox.setCurrentIndex(index)
            if init:
                self.update_rotation_list(0)
            self.profileComboBox.setDisabled(False)
        else:
            self.profileComboBox.setDisabled(True)
            self.profileComboBox.addItem('--Нужно добавить профайл--', None)

    def update_rotation_list(self, index=None):
        profile = self.get_current_profile()

        while self.rotationTable.rowCount() > 0:
            self.rotationTable.removeRow(0)
        if index != -1:
            for i, rotation in enumerate(profile.rotations):
                self.rotationTable.insertRow(i)
                rotation = profile.rotations[i]
                name_item = QTableWidgetItem(rotation.name)
                name_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.rotationTable.setItem(i, 0, name_item)
                run_button = QPushButton("Пуск" if not rotation.is_run else 'Стоп')
                run_button.clicked.connect(self.on_click_run_button(i))
                run_button_index = self.rotationTable.model().index(i, 1)
                self.rotationTable.setIndexWidget(run_button_index, run_button)

    def on_click_run_button(self, index):
        def wrap(*args, **kwargs):
            profile = self.get_current_profile()
            button = self.rotationTable.cellWidget(index, 1)
            button.setDisabled(True)
            rotation = profile.rotations[index]
            if rotation.is_run:
                rotation.stop()
            else:
                rotation.run()
            button.setDisabled(False)
            self.update_rotation_list()

        return wrap

    def get_current_profile(self):
        print(123, self.profileComboBox.currentData(), self.profileComboBox.currentIndex())
        return self.profileComboBox.currentData()

    def on_remove_rotation(self, index):
        profile = self.get_current_profile()

        def wrap():
            rotation = profile.rotations[index]
            logging.info("Удаление ротации: {}".format(rotation.name))
            profile.remove_rotation(rotation)
            profile.save()
            self.update_rotation_list()

        return wrap

    def on_add_new_profile(self):
        dialog = NewProfileDialog(self)
        result = dialog.exec_()
        new_profile_name = dialog.get_profile_name().strip()
        if new_profile_name and result == QDialog.Accepted:
            new_profile = Profile.create(new_profile_name)
            logging.info('Создание нового профайла: {}'.format(new_profile.name))
            self.update_profile_list(new_profile)
