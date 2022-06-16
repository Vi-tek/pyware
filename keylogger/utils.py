import ctypes
from ctypes import c_long
from dataclasses import dataclass

user32 = ctypes.WinDLL("user32", use_last_error=True)
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)


@dataclass(init=True)
class Vector2:
    x: c_long or int
    y: c_long or int
