from Loggers import *


class MouseLogger(Logger):
    def __init__(self, handler: any, quit_button: int = None):
        super(MouseLogger, self).__init__(LoggerEnum.MOUSE.value, quit_button)
        self.handler = handler

    def _process_body(self, nCode, wParam, lParam):
        if wParam == self.quit_input:
            self.stop_listener()

        self.handler(MouseEvent(wParam, ...))
