from LoggerCore import *
from collections import namedtuple


class MouseCodes:
    MOVE = 0x200
    LMB_DOWN = 0x201
    LMB_UP = 0x202
    RMB_DOWN = 0x204
    RMB_UP = 0x205
    WHEEL_DOWN = 0x207
    WHEEL_UP = 0x208
    WHEEL = 0x20A
    MOUSE_BUTTON_DOWN = 0x20B
    MOUSE_BUTTON_UP = 0x20C


MouseEvent = namedtuple("MouseEvents", ["Button", "Window"])  # window title


class MouseLogger(Logger):
    def __init__(self, handler: any, quit_button: int = None):
        super(MouseLogger, self).__init__(LoggerEnum.MOUSE.value, quit_button)
        self.handler = handler

    def _process_body(self, nCode, wParam, lParam):
        if wParam == self.quit_input:
            self.stop_listener()

        self.handler(MouseEvent(wParam))
