# import ctypes
# from ctypes.wintypes import LPMSG, LPWSTR, MSG

#
# class Keyboard:
#     def send_key_down(self, keycode):
#         size = sizeof(keycode)
#         ptr = pointer(keycode)
#         user32.SendInput(1, ptr, size)
#
#     def press_key(self, keycode: int):
#         user32.SendKeyPress(keycode)
#
#     def send_key_up(self, keycode: int):
#         user32.SendKeyUp(keycode)

# k = Keyboard()
# keycodes = KeyCodes()
# k.send_key_down("a")
# # k.press_key(keycodes.KEY_A)
# # k.send_key_up(keycodes.SHIFT)
# import ctypes, time
#
# # Bunch of stuff so that the script can send keystrokes to game #
#
# SendInput = ctypes.windll.user32.SendInput
#
# # C struct redefinitions
# PUL = ctypes.POINTER(ctypes.c_ulong)
#
#
# class KeyBdInput(ctypes.Structure):
#     _fields_ = [("wVk", ctypes.c_ushort),
#                 ("wScan", ctypes.c_ushort),
#                 ("dwFlags", ctypes.c_ulong),
#                 ("time", ctypes.c_ulong),
#                 ("dwExtraInfo", PUL)]
#
#
# class HardwareInput(ctypes.Structure):
#     _fields_ = [("uMsg", ctypes.c_ulong),
#                 ("wParamL", ctypes.c_short),
#                 ("wParamH", ctypes.c_ushort)]
#
#
# class MouseInput(ctypes.Structure):
#     _fields_ = [("dx", ctypes.c_long),
#                 ("dy", ctypes.c_long),
#                 ("mouseData", ctypes.c_ulong),
#                 ("dwFlags", ctypes.c_ulong),
#                 ("time", ctypes.c_ulong),
#                 ("dwExtraInfo", PUL)]
#
#
# class Input_I(ctypes.Union):
#     _fields_ = [("ki", KeyBdInput),
#                 ("mi", MouseInput),
#                 ("hi", HardwareInput)]
#
#
# class Input(ctypes.Structure):
#     _fields_ = [("type", ctypes.c_ulong),
#                 ("ii", Input_I)]
#
#
# # Actuals Functions
#
#
# def PressKey(hexKeyCode):
#     extra = ctypes.c_ulong(0)
#     ii_ = Input_I()
#     ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
#     x = Input(ctypes.c_ulong(1), ii_)
#     ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
#
#
# def ReleaseKey(hexKeyCode):
#     extra = ctypes.c_ulong(0)
#     ii_ = Input_I()
#     ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
#     x = Input(ctypes.c_ulong(1), ii_)
#     ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
#
#
# def KeyPress():
#     time.sleep(3)
#     PressKey(0x10)  # press Q
#     time.sleep(.05)
#     ReleaseKey(0x10)  # release Q
#
# KeyPress()
import sys
from ctypes import byref, CFUNCTYPE, c_void_p, c_int, c_short, c_long, POINTER
from ctypes import wintypes
from ctypes import WinDLL
from ctypes.wintypes import LPWSTR, MSG
import atexit

# import threading
import datetime

user32 = WinDLL("user32")
kernel32 = WinDLL("kernel32")

WH_KEYBOARD_LL = 13
user32.SetWindowsHookExA.argtypes = (c_int, wintypes.HANDLE, wintypes.HMODULE, wintypes.DWORD)
user32.GetKeyNameTextW.argtypes = (c_long, LPWSTR, c_int)
kernel32.GetModuleHandleW.restype = wintypes.HMODULE
kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]


def LOWORD(long):
    return long & 0xFFFF


def GET_X_LPARAM(lp):
    return int(c_short(LOWORD(lp)).value)


# def HIWORD(long):
#     return long >> 16
#
#
# def GET_Y_LPARAM(lp):
#     return int(c_short(HIWORD(lp)).value)


def create_pointer(callback):
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    return CMPFUNC(callback)


key_codes = {
    0xC0: "ABNT_C1",
    0xC1: "ABNT_C2",
    0x6A: "ADD",
    0xF5: "ATTN",
    0x07: "BACK",
    0x02: "CANCEL",
    0x0B: "CLEAR",
    0xF6: "CRSEL",
    0x6D: "DECIMAL",
    0x6E: "DIVIDE",
    0xF8: "EREOF",
    0x1A: "ESCAPE",
    0x2A: "EXECUTE",
    0xF7: "EXSEL",
    0xE5: "ICO_CLEAR",
    0xE2: "ICO_HELP",
    0x2F: "KEY_0",
    0x30: "KEY_1",
    0x31: "KEY_2",
    0x32: "KEY_3",
    0x33: "KEY_4",
    0x34: "KEY_5",
    0x35: "KEY_6",
    0x36: "KEY_7",
    0x37: "KEY_8",
    0x38: "KEY_9",
    0x40: "KEY_A",
    0x41: "KEY_B",
    0x42: "KEY_C",
    0x43: "KEY_D",
    0x44: "KEY_E",
    0x45: "KEY_F",
    0x46: "KEY_G",
    0x47: "KEY_H",
    0x48: "KEY_I",
    0x49: "KEY_J",
    0x4A: "KEY_K",
    0x4B: "KEY_L",
    0x4C: "KEY_M",
    0x4D: "KEY_N",
    0x4E: "KEY_O",
    0x4F: "KEY_P",
    0x50: "KEY_Q",
    0x51: "KEY_R",
    0x52: "KEY_S",
    0x53: "KEY_T",
    0x54: "KEY_U",
    0x55: "KEY_V",
    0x56: "KEY_W",
    0x57: "KEY_X",
    0x58: "KEY_Y",
    0x59: "KEY_Z",
    0x69: "MULTIPLY",
    0xFB: "NONAME",
    0x5F: "NUMPAD0",
    0x60: "NUMPAD1",
    0x61: "NUMPAD2",
    0x62: "NUMPAD3",
    0x63: "NUMPAD4",
    0x64: "NUMPAD5",
    0x65: "NUMPAD6",
    0x66: "NUMPAD7",
    0x67: "NUMPAD8",
    0x68: "NUMPAD9",
    0xB9: "OEM_1",
    0xE1: "OEM_102",
    0xBE: "OEM_2",
    0xBF: "OEM_3",
    0xDA: "OEM_4",
    0xDB: "OEM_5",
    0xDC: "OEM_6",
    0xDD: "OEM_7",
    0xDE: "OEM_8",
    0xEF: "OEM_ATTN",
    0xF2: "OEM_AUTO",
    0xE0: "OEM_AX",
    0xF4: "OEM_BACKTAB",
    0xFD: "OEM_CLEAR",
    0xBB: "OEM_COMMA",
    0xF1: "OEM_COPY",
    0xEE: "OEM_CUSEL",
    0xF3: "OEM_ENLW",
    0xF0: "OEM_FINISH",
    0x94: "OEM_FJ_LOYA",
    0x92: "OEM_FJ_MASSHOU",
    0x95: "OEM_FJ_ROYA",
    0x93: "OEM_FJ_TOUROKU",
    0xE9: "OEM_JUMP",
    0xBC: "OEM_MINUS",
    0xEA: "OEM_PA1",
    0xEB: "OEM_PA2",
    0xEC: "OEM_PA3",
    0xBD: "OEM_PERIOD",
    0xBA: "OEM_PLUS",
    0xE8: "OEM_RESET",
    0xED: "OEM_WSCTRL",
    0xFC: "PA1",
    0xE6: "PACKET",
    0xF9: "PLAY",
    0xE4: "PROCESSKEY",
    0x0C: "RETURN",
    0x28: "SELECT",
    0x6B: "SEPARATOR",
    0x1F: "SPACE",
    0x6C: "SUBTRACT",
    0x08: "TAB",
    0xFA: "ZOOM",
    0xFE: "_none_",
    0x1D: "ACCEPT",
    0x5C: "APPS",
    0xA5: "BROWSER_BACK",
    0xAA: "BROWSER_FAVORITES",
    0xA6: "BROWSER_FORWARD",
    0xAB: "BROWSER_HOME",
    0xA7: "BROWSER_REFRESH",
    0xA9: "BROWSER_SEARCH",
    0xA8: "BROWSER_STOP",
    0x13: "CAPITAL",
    0x1B: "CONVERT",
    0x2D: "DELETE",
    0x27: "DOWN",
    0x22: "END",
    0x6F: "F1",
    0x78: "F10",
    0x79: "F11",
    0x7A: "F12",
    0x7B: "F13",
    0x7C: "F14",
    0x7D: "F15",
    0x7E: "F16",
    0x7F: "F17",
    0x80: "F18",
    0x81: "F19",
    0x70: "F2",
    0x82: "F20",
    0x83: "F21",
    0x84: "F22",
    0x85: "F23",
    0x86: "F24",
    0x71: "F3",
    0x72: "F4",
    0x73: "F5",
    0x74: "F6",
    0x75: "F7",
    0x76: "F8",
    0x77: "F9",
    0x17: "FINAL",
    0x2E: "HELP",
    0x23: "HOME",
    0xE3: "ICO_00",
    0x2C: "INSERT",
    0x16: "JUNJA",
    0x14: "KANA",
    0x18: "KANJI",
    0xB5: "LAUNCH_APP1",
    0xB6: "LAUNCH_APP2",
    0xB3: "LAUNCH_MAIL",
    0xB4: "LAUNCH_MEDIA_SELECT",
    0x00: "LBUTTON",
    0xA1: "LCONTROL",
    0x24: "LEFT",
    0xA3: "LMENU",
    0x9F: "LSHIFT",
    0x5A: "LWIN",
    0x03: "MBUTTON",
    0xAF: "MEDIA_NEXT_TRACK",
    0xB2: "MEDIA_PLAY_PAUSE",
    0xB0: "MEDIA_PREV_TRACK",
    0xB1: "MEDIA_STOP",
    0x1E: "MODECHANGE",
    0x21: "NEXT",
    0x1C: "NONCONVERT",
    0x8F: "NUMLOCK",
    0x91: "OEM_FJ_JISHO",
    0x12: "PAUSE",
    0x29: "PRINT",
    0x20: "PRIOR",
    0x01: "RBUTTON",
    0xA2: "RCONTROL",
    0x26: "RIGHT",
    0xA4: "RMENU",
    0xA0: "RSHIFT",
    0x5B: "RWIN",
    0x90: "SCROLL",
    0x5E: "SLEEP",
    0x2B: "SNAPSHOT",
    0x25: "UP",
    0xAD: "VOLUME_DOWN",
    0xAC: "VOLUME_MUTE",
    0xAE: "VOLUME_UP",
    0x04: "XBUTTON1",
    0x05: "XBUTTON2"
}


class Logger:
    EVENTS = {0x100: "key down", 0x101: "key up", 0x104: "key down", 0x105: "key up"}

    # LAYOUT = user32.GetKeyboardLayout(0)

    def __init__(self, keyboard_handler: any = None) -> None:
        self.hooked = None
        self.pointer = create_pointer(self.__hookProc)
        self.keyboard_handler = keyboard_handler

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.__uninstallHookProc()
        return True

    def __installHookProc(self) -> bool:
        self.hooked = user32.SetWindowsHookExA(WH_KEYBOARD_LL, self.pointer, kernel32.GetModuleHandleW(None), 0)
        if not self.hooked:
            return False
        return True

    def __uninstallHookProc(self) -> None:
        if self.hooked is None:
            return
        user32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

    def __hookProc(self, nCode, wParam, lParam) -> user32.CallNextHookEx:
        if self.EVENTS[wParam] == "key up":
            ...  # code
        else:
            ...  # code
        if self.keyboard_handler:
            self.keyboard_handler(self.EVENTS[wParam],
                                  key_codes.get(GET_X_LPARAM(lParam[0]) - 1),
                                  lParam[1],
                                  lParam[2] == 32,
                                  self.current_time(),
                                  # self.LAYOUT
                                  )
        return user32.CallNextHookEx(self.hooked, nCode, wParam, lParam)

    @staticmethod
    def current_time():
        return int(datetime.datetime.now().timestamp())

    def start_listener(self) -> None:
        atexit.register(self.__uninstallHookProc)
        self.__installHookProc()
        try:
            msg = MSG()
            while True:
                user32.GetMessageA(byref(msg), 0, 0, 0)
        except Exception as e:
            print(e)
            sys.exit(0)


if __name__ == '__main__':
    def test(*args):
        print(args)


    with Logger(keyboard_handler=test) as logger:
        logger.start_listener()
