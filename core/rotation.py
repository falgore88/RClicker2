import copy
import logging
import traceback

import keyboard
from PySide6.QtCore import QObject, Signal, QThread
from pynput.keyboard import Controller

from libs.utils import get_pixel_color


class MySignal(QObject):
    sig = Signal(str)


class RotationHealThread(QThread):
    color_map = {
        "#FFFFE0": "y",
        "#0000FE": "F1",
        "#F3FEF8": "F2",
        "#EC7DEC": "F3",
        "#EEFEFE": "F4",
        "#D76AD3": "F5",
        "#EEFEEE": "F6",
        "#DEFEFE": "F7",
        "#8E6AD8": "F8",
        "#EEF6FE": "F9",
        "#F3F3F3": "F10",
        "#F6F6FE": "F11",
        "#FEFEEE": "F12",
        "#FEF8F8": "SHIFT+F1",
        "#FEF8EE": "SHIFT+F2",
        "#44007D": "SHIFT+F3",
        "#FEF3EC": "SHIFT+F4",
        "#FBF3E4": "SHIFT+F5",
        "#FEEEF3": "SHIFT+F6",
        "#7662EC": "SHIFT+F7",
        "#F8EEE4": "SHIFT+F8",
        "#94F994": "SHIFT+F9",
        "#F8E9D4": "SHIFT+F10",
        "#FEE2DF": "SHIFT+F11",
        "#FEBDC8": "SHIFT+F12",
        "#FEB2BE": "ALT+F1",
        "#FE63B0": "ALT+F2",
        "#D86A8E": "ALT+F3",
        # "#8BEC8B": "ALT+F4",
        "#F87B6D": "ALT+F8",
        "#E79175": "ALT+F9",
        "#FEF6DA": "ALT+F10",
        "#FEE9CA": "ALT+F11",
        "#FEE2C1": "ALT+F12",
        "#8AB98A": "CTRL+F1",
        "#FEDCA9": "CTRL+F2",
        "#60CAA6": "CTRL+F3",
        "#F3DCAF": "CTRL+F4"
    }

    def __init__(self, rotation_data, parent=None):
        super(RotationHealThread, self).__init__(parent)
        self.rotation_data = rotation_data
        self._run = False
        self._keyword_controller = Controller()
        self.signal = MySignal()

    def run(self, *args, **kwargs):
        try:
            while True:
                if keyboard.is_pressed(self.rotation_data['bind']):
                    addon_coords = map(int, self.rotation_data.get('addon_coords', []))
                    addon_color = get_pixel_color(*addon_coords).upper()
                    member_bind = self.color_map.get(addon_color)
                    if member_bind:
                        keyboard.press_and_release(member_bind.lower())
                        self.msleep(10)

                        for ability in self.rotation_data['abilities']:
                            coords = map(int, ability.get('coords', []))
                            color = ability.get('color')
                            bind = ability.get('bind')
                            pixel_color = get_pixel_color(*coords)
                            if coords and pixel_color == color:
                                self._keyword_controller.press(bind)
                                self._keyword_controller.release(bind)
                                # self.signal.sig.emit('Ротация "{}" использует "{}"'.format(self.rotation_data['name'], ability['name']))
                                self.msleep(self.rotation_data['ability_timeout'])
                                break
                self.msleep(self.rotation_data['global_timeout'])
        except Exception as e:
            self.signal.sig.emit(traceback.format_exc())


class RotationThread(QThread):
    def __init__(self, rotation_data, parent=None):
        super(RotationThread, self).__init__(parent)
        self.rotation_data = rotation_data
        self._run = False
        self._keyword_controller = Controller()
        self.signal = MySignal()

    def run(self, *args, **kwargs):
        try:
            while True:
                if keyboard.is_pressed(self.rotation_data['bind']):
                    for ability in self.rotation_data['abilities']:
                        coords = map(int, ability.get('coords', []))
                        color = ability.get('color')
                        bind = ability.get('bind')
                        pixel_color = get_pixel_color(*coords)
                        if coords and pixel_color == color:
                            self._keyword_controller.press(bind)
                            self._keyword_controller.release(bind)
                            # self.signal.sig.emit('Ротация "{}" использует "{}"'.format(self.rotation_data['name'], ability['name']))
                            self.msleep(self.rotation_data['ability_timeout'])
                            break
                self.msleep(self.rotation_data['global_timeout'])
        except Exception as e:
            self.signal.sig.emit(traceback.format_exc())


class Rotation(object):
    TYPE_BATTLE = 1
    TYPE_HEAL = 2

    BASE_STRUCTURE = {
        'name': 'Новая ротация',
        'bind': '',
        'abilities': [],
        'ability_timeout': 50,
        'global_timeout': 30,
        'type': TYPE_BATTLE
    }

    def __init__(self, profile, rotation_data=None, is_new=False):
        if rotation_data is None:
            rotation_data = self.BASE_STRUCTURE
        self._profile = profile
        self.is_new = is_new
        self._rotation_data = rotation_data
        self._process = None

    def __repr__(self):
        return '<Profile "{}" rotation: "{}">'.format(self._profile, self.name)

    def run(self):
        if self.type == self.TYPE_BATTLE:
            self._process = RotationThread(self._rotation_data)
        else:
            self._process = RotationHealThread(self._rotation_data)
        self._process.setTerminationEnabled(True)
        self._process.signal.sig.connect(self._logging_thread)
        self._process.start()
        logging.info('Пуск ротации: {}'.format(self.name))

    def stop(self):
        if self._process:
            self._process.terminate()
            self._process.wait()
            self._process = None
            logging.info("Остановка ротации: {}".format(self.name))

    def _logging_thread(self, comment):
        logging.info(comment)

    @property
    def type(self):
        return self._rotation_data.get('type', self.TYPE_BATTLE)

    @property
    def addon_coords(self):
        return self._rotation_data.get('addon_coords', [])

    def set_addon_coords(self, coords):
        self._rotation_data['addon_coords'] = coords

    def set_global_timeout(self, timeout):
        self._rotation_data['global_timeout'] = timeout

    def set_ability_timeout(self, timeout):
        self._rotation_data['ability_timeout'] = timeout

    def set_name(self, name):
        self._rotation_data['name'] = name

    def set_bind(self, bind):
        self._rotation_data['bind'] = bind

    @property
    def is_run(self):
        return self._process and self._process.isRunning()

    @property
    def name(self):
        return self._rotation_data['name']

    @property
    def bind(self):
        return self._rotation_data['bind']

    @property
    def ability_timeout(self):
        return self._rotation_data['ability_timeout']

    @property
    def global_timeout(self):
        return self._rotation_data['global_timeout']

    @property
    def abilities(self):
        return self._rotation_data['abilities']

    def set_abilities(self, abilities):
        self._rotation_data['abilities'] = abilities

    def remove_ability(self, ability):
        self._rotation_data['abilities'].remove(ability)

    def serialize(self):
        return self._rotation_data

    @classmethod
    def deserialize(cls, profile, rotation_data):
        return cls(profile, rotation_data)

    @classmethod
    def create(cls, profile, rotation_type=TYPE_BATTLE):
        rotation_data = copy.deepcopy(cls.BASE_STRUCTURE)
        rotation_data['type'] = rotation_type
        return cls(profile, rotation_data, is_new=True)

    def save(self):
        if self.is_new:
            self.is_new = False
            self._profile.add_rotation(self)
        return self
