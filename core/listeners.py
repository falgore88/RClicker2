from PySide6.QtCore import QThread
from pynput import mouse, keyboard


class ListenerMouseEvent(QThread):
    def __init__(self, on_click=None, on_move=None, on_scroll=None):
        super(ListenerMouseEvent, self).__init__()
        self.on_click = on_click
        self.on_move = on_move
        self.on_scroll = on_scroll
        self._listener = None

    def run(self, *args, **kwargs):
        self._listener = mouse.Listener(
            on_click=self.on_click,
            on_move=self.on_move,
            on_scroll=self.on_scroll
        )

        with self._listener as l:
            while True:
                if not l.running:
                    break
                self.msleep(5)

    def terminate(self, *args, **kwargs):
        if self._listener:
            self._listener.stop()
            self._listener.join()
        return super(ListenerMouseEvent, self).terminate(*args, **kwargs)


class ListenerKeyboardEvent(QThread):
    def __init__(self, on_press=None, on_release=None):
        super(ListenerKeyboardEvent, self).__init__()
        self.on_press = on_press
        self.on_release = on_release
        self._listener = None
        self._killed = False

    def run(self, *args, **kwargs):
        self._listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        with self._listener as l:
            while True:
                if not l.running:
                    break
                self.msleep(5)

    def terminate(self, *args, **kwargs):
        if self._listener:
            self._listener.stop()
            self._listener.join()
        return super(ListenerKeyboardEvent, self).terminate(*args, **kwargs)
