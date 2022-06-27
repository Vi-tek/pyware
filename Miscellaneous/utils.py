from dataclasses import dataclass

from ctypes import *
from ctypes.wintypes import *


class RECT(Structure):
    _fields_ = [("left", LONG),
                ("top", LONG),
                ("right", LONG),
                ("bottom", LONG)]


user32 = windll.user32
kernel32 = windll.kernel32

user32.SetWindowsHookExA.argtypes = (c_int, HANDLE, HINSTANCE, DWORD)
user32.GetKeyboardLayoutNameA.argtypes = (DWORD,)

user32.GetMessageA.argtypes = POINTER(MSG), HWND, UINT, UINT
user32.GetMessageA.restype = BOOL

user32.LoadKeyboardLayoutA.argtypes = (LPSTR, UINT)

kernel32.GetModuleHandleW.restype = HMODULE
kernel32.GetModuleHandleW.argtypes = [LPCWSTR]

kernel32.GetCurrentProcessId.argtypes = ()
kernel32.GetCurrentProcessId.restype = DWORD


def LOWORD(long):
    return long & 0xFFFF


def GET_X_LPARAM(lp):
    return int(c_short(LOWORD(lp)).value)


def HIWORD(long):
    return long >> 16


def GET_Y_LPARAM(lp):
    return int(c_short(HIWORD(lp)).value)


@dataclass(init=True)
class Vector2:
    x: c_long or int
    y: c_long or int
