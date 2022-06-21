import abc
from enum import Enum
from misc.utils import *

import datetime
import atexit


class LoggerEnum(Enum):
    KEYBOARD = 13
    MOUSE = 14


class Logger(abc.ABC):
    def __init__(self, logger_type: int, quit_input: int):
        self.logger_type = logger_type
        self.hooked = None
        self.pointer = self._callback(self._hookProc)
        self.quit_input = quit_input

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._uninstallHookProc()
        return True

    def _installHookProc(self):
        self.hooked = user32.SetWindowsHookExA(
            self.logger_type,
            self.pointer,
            kernel32.GetModuleHandleW(None),
            0
        )

        if not self.hooked:
            return False
        return True

    def _uninstallHookProc(self):
        if self.hooked is None:
            return
        user32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

    @abc.abstractmethod
    def _process_body(self, nCode, wParam, lParam):
        ...

    def _hookProc(self, nCode, wParam, lParam):
        self._process_body(nCode, wParam, lParam)

        return user32.CallNextHookEx(self.hooked, nCode, wParam, lParam)

    @staticmethod
    def _current_time():
        return int(datetime.datetime.now().timestamp())

    @staticmethod
    def _callback(callback_):
        CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
        return CMPFUNC(callback_)

    @staticmethod
    def stop_listener():
        process_id = kernel32.GetCurrentProcessId()
        handle = kernel32.OpenProcess(1, False, process_id)
        kernel32.TerminateProcess(handle, -1)
        kernel32.CloseHandle(handle)

    def start_listener(self):
        atexit.register(self._uninstallHookProc)
        self._installHookProc()
        msg = MSG()
        user32.GetMessageA(byref(msg), 0, 0, 0)
