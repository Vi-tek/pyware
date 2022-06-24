from Loggers import *


class MouseLogger(Logger):
    def __init__(self, handler: any, quit_button: int = None):
        super(MouseLogger, self).__init__(LoggerEnum.MOUSE.value, quit_button)
        self.handler = handler

    def _process_body(self, nCode, wParam, lParam):
        if wParam == self.quit_input:
            self.stop_listener()
        self.handler(
            MouseEvent(wParam,  # mouse button
                       Vector2(GET_X_LPARAM(lParam[0]), lParam[0] >> 32),  # mouse position
                       self._get_active_window_title())  # active window title
        )
