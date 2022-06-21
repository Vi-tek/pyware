from misc.utils import *
import time


class MouseFlags:
    LEFTDOWN = 0x02
    LEFTUP = 0x04
    RIGHTDOWN = 0x08
    RIGHTUP = 0x10
    MIDDLEDOWN = 0x20
    MIDDLEUP = 0x40
    MOVE = 0x01


class Mouse:
    def __init__(self):
        self.mouse_flags = MouseFlags()

    @staticmethod
    def get_mouse_pos() -> Vector2:
        pt = POINT()
        user32.GetCursorPos(byref(pt))
        return Vector2(pt.x, pt.y)

    @staticmethod
    def set_mouse_pos(pos: Vector2) -> None:
        user32.SetCursorPos(pos.x, pos.y)

    def left_click(self, pos: Vector2) -> None:
        user32.mouse_event(self.mouse_flags.LEFTDOWN | self.mouse_flags.LEFTUP, pos.x, pos.y, 0, 0)

    def left_double_click(self, pos: Vector2, click_delay: int = .01) -> None:
        self.left_click(pos)
        time.sleep(click_delay)
        self.left_click(pos)

    def right_click(self, pos: Vector2) -> None:
        user32.mouse_event(self.mouse_flags.RIGHTDOWN | self.mouse_flags.RIGHTUP, pos.x, pos.y, 0, 0)

    def right_double_click(self, pos: Vector2, click_delay: int = .01) -> None:
        self.right_click(pos)
        time.sleep(click_delay)
        self.right_click(pos)

    def middle_click(self, pos: Vector2) -> None:
        user32.mouse_event(self.mouse_flags.MIDDLEDOWN | self.mouse_flags.MIDDLEUP, pos.x, pos.y, 0, 0)


if __name__ == '__main__':
    m = Mouse()
    print(m.get_mouse_pos())
    m.left_click(m.get_mouse_pos())
