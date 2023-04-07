import logging

from PySide6.QtWidgets import QDialog, QMenu, QTableWidgetItem, QPushButton, QHeaderView, QMessageBox
from pynput import mouse

from core.listeners import ListenerMouseEvent, ListenerKeyboardEvent
from core.rotation import Rotation
from libs.utils import get_pixel_color
from ui.dialogs.RotationBattleDialog import Ui_Dialog


class RotationBattleDialog(Ui_Dialog):
    def __init__(self, profile, parent=None, rotation=None):
        self.profile = profile
        self.rotation = rotation or Rotation.create(self.profile, Rotation.TYPE_BATTLE)
        self.dialog = QDialog(parent)
        self._mouse_bind_listener = None
        self._keyboard_bind_listener = None
        self.setupUi(self.dialog)

    def setupUi(self, dialog):
        super(RotationBattleDialog, self).setupUi(dialog)
        self.cancelButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(self.on_save)

        self.rotationNameTextField.setText(self.rotation.name)
        self.globalTimeoutField.setValue(self.rotation.global_timeout)
        self.abilityTimeoutField.setValue(self.rotation.ability_timeout)
        self.bindButton.setText(self.rotation.bind or 'Нажмите')

        for ability in self.rotation.abilities:
            self.add_new_ability(ability)

        self.bindButton.clicked.connect(self.on_bind_button(self.bindButton))

        self.update_ability_table_size()

        self.abilityTable.customContextMenuRequested.connect(self.on_ability_menu)

    def on_ability_menu(self, position):

        row = self.abilityTable.rowAt(position.y())
        menu = QMenu()
        add_ability_action = menu.addAction('Добавить аббилку')
        add_ability_action.triggered.connect(self.on_add_new_ability)
        if row != -1:
            remove_rotation_action = menu.addAction("Удалить абилку")
            remove_rotation_action.triggered.connect(self.on_remove_ability(row))
        menu.exec_(self.abilityTable.mapToGlobal(position))

    def on_remove_ability(self, index):
        def wrap():
            self.abilityTable.removeRow(index)

        return wrap

    def on_add_new_ability(self):
        self.add_new_ability()
        self.update_ability_table_size()

    def add_new_ability(self, ability_data=None):
        if ability_data is None:
            ability_data = {}
        row_count = self.abilityTable.rowCount()
        self.abilityTable.insertRow(row_count)
        self.abilityTable.setItem(row_count, 0, QTableWidgetItem(ability_data.get('name') or "Новая абилка {}".format(row_count + 1)))

        bind_button = QPushButton(ability_data.get('bind') or 'Нажмите')
        bind_button.clicked.connect(self.on_bind_button(bind_button))
        bind_button_index = self.abilityTable.model().index(row_count, 1)
        self.abilityTable.setIndexWidget(bind_button_index, bind_button)

        color_item = QTableWidgetItem(ability_data.get('color') or "")

        coord_button = QPushButton(",".join(ability_data.get('coords', [])) or "Нажмите")
        coord_button_index = self.abilityTable.model().index(row_count, 2)
        coord_button.clicked.connect(self.on_set_ability_coors(coord_button, color_item))
        self.abilityTable.setIndexWidget(coord_button_index, coord_button)

        self.abilityTable.setItem(row_count, 3, color_item)

    def update_ability_table_size(self):
        header = self.abilityTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

    def on_bind_button(self, btn):
        def wrap():
            self._start_keyboard_bind_thread(self._on_press_bind, self.on_release_bind(btn))

        return wrap

    def _on_press_bind(self, *args, **kwargs):
        pass

    def _start_keyboard_bind_thread(self, on_press, on_release):
        if self._keyboard_bind_listener and self._keyboard_bind_listener.isRunning():
            self._keyboard_bind_listener.terminate()
            self._keyboard_bind_listener.wait()

        self._keyboard_bind_listener = ListenerKeyboardEvent(on_press, on_release)
        self._keyboard_bind_listener.start()

    def on_set_ability_coors(self, btn, color_item):
        def wrap():
            self._start_mouse_bind_thread(self.on_set_ability_coords_release(btn, color_item))

        return wrap

    def _start_mouse_bind_thread(self, on_click):
        if self._mouse_bind_listener and self._mouse_bind_listener.isRunning():
            self._mouse_bind_listener.terminate()
            self._mouse_bind_listener.wait()
        self._mouse_bind_listener = ListenerMouseEvent(
            on_click=on_click
        )
        self._mouse_bind_listener.start()

    def on_set_ability_coords_release(self, btn, color_item):
        def wrap(x, y, button, pressed):
            if pressed and button == mouse.Button.left:
                btn.setText('{},{}'.format(x, y))
                color_item.setText(get_pixel_color(x, y))
                return False

        return wrap

    def on_release_bind(self, btn):
        def wrap(key):
            keypress = str(key).replace("'", "")
            btn.setText(keypress)
            return False

        return wrap

    def close(self):
        self.dialog.close()

    def exec_(self, *args, **kwargs):
        return self.dialog.exec_(*args, **kwargs)

    def on_save(self):
        row_count = self.abilityTable.rowCount()
        name = self.rotationNameTextField.text()

        ability_timeout = self.abilityTimeoutField.value()

        global_timeout = self.globalTimeoutField.value()

        rotation_bind = self.bindButton.text()
        if rotation_bind == 'Нажмите':
            rotation_bind = None

        abilities = []
        for i in range(row_count):
            ability_name = self.abilityTable.item(i, 0).text()
            bind = self.abilityTable.cellWidget(i, 1).text()
            coors = self.abilityTable.cellWidget(i, 2).text()
            color = self.abilityTable.item(i, 3).text()
            abilities.append({
                'bind': bind,
                'coords': coors.split(','),
                'color': color,
                'name': ability_name
            })

        if not all((name, ability_timeout, global_timeout, rotation_bind, abilities)):
            msgBox = QMessageBox.warning(
                self.dialog,
                "Ошибка",
                "Заполните все поля и создайте хотябы одну абилку"
            )
        else:
            self.rotation.set_name(name)
            self.rotation.set_ability_timeout(ability_timeout)
            self.rotation.set_global_timeout(global_timeout)
            self.rotation.set_bind(rotation_bind)
            self.rotation.set_abilities(abilities)
            self.rotation.save()
            logging.info("Сохранение ротации: {}".format(self.rotation.name))
            self.close()
