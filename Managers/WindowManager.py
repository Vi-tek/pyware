import time

from Miscellaneous.utils import *


class ToInt(int):
    def __new__(cls, value):
        return int(value)


class WindowManager:
    def __init__(self):
        self.handler = None
        self.rect = RECT()

    @property
    def size(self):
        # def size(self, handler: int = None):
        #     if handler is None:
        #         handler = self.handler
        user32.GetWindowRect(self.handler, byref(self.rect))
        width = self.rect.right - self.rect.left
        height = self.rect.bottom - self.rect.top
        return width, height

    @property
    def position(self):
        user32.GetWindowRect(self.handler, byref(self.rect))
        return Vector2(ToInt(self.rect.left), ToInt(self.rect.top))

    def set_position(self, pos: Vector2):
        width, height = self.size
        user32.SetWindowPos(self.handler, 0, pos.x, pos.y, width, height, 0)

    def set_size(self, width, height):
        pos = self.position
        user32.SetWindowPos(self.handler, 0, pos.x, pos.y, width, height, 0)

    def __show_modes(self, window_message: int):
        user32.ShowWindow(self.handler, window_message)

    def set_foreground(self):
        ...

    def show(self):
        """
        Shows the window.
        :return: None
        """
        self.__show_modes(5)

    def hide(self):
        """
        Hides the window. No one can see it ;)
        :return: None
        """
        self.__show_modes(0)

    def minimize(self):
        self.__show_modes(2)

    def maximize(self):
        self.__show_modes(3)

    def brint_to_top(self, show: bool = False):
        user32.BringWindowToTop(self.handler)
        if show:
            self.show()
        # user32.SetForegroundWindow(self.handler)

    def is_active(self):
        ...

    def is_hidden(self):
        ...

    def is_visible(self):
        ...

    def close(self):
        ...

    # def get_window_info(self, handler):
    #     return user32.GetWindowInfo(handler, )

    def get_active_window(self):
        self.handler = user32.GetForegroundWindow()
        return self

    def get_all_window_titles(self) -> list:
        EnumWindows = user32.EnumWindows
        EnumWindowsProc = CFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
        IsWindowVisible = user32.IsWindowVisible

        titles = []
        self_ = self

        def foreach_window(hwnd, lParam):
            if IsWindowVisible(hwnd):
                self_.handler = hwnd
                if len(self_.title) > 0:
                    titles.append(self_.title)
            return True

        EnumWindows(EnumWindowsProc(foreach_window), 0)
        return titles

    def get_window_by_title(self, title: str):
        self.handler = user32.FindWindowW(None, title)
        return self

    @property
    def title(self):
        buffer = create_unicode_buffer(256)
        user32.GetWindowTextW(self.handler, buffer, 256)
        return buffer.value


if __name__ == '__main__':
    time.sleep(2)
    s = WindowManager()
    # s.get_active_window()
    a = s.get_all_window_titles()
    print(a)
    s.get_window_by_title('')
    s.set_position(Vector2(0, 0))
    # s.set_size(1000, 200)
    s.brint_to_top(show=True)
    # s.hide()
    s.show()
    s.maximize()
    s.minimize()
