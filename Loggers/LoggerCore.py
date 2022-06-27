import abc
import atexit
import datetime
from Miscellaneous import *
from Managers.WindowManager import WindowManager


class Logger(abc.ABC):
    def __init__(self, logger_type: int, quit_input: int):
        self._logger_type = logger_type
        self._hooked = None
        self._pointer = self._callback(self._hookProc)
        self._quit_input = quit_input
        self._wm = WindowManager()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._uninstallHookProc()
        return True

    def _installHookProc(self):
        self._hooked = user32.SetWindowsHookExA(
            self._logger_type,
            self._pointer,
            kernel32.GetModuleHandleW(None),
            0
        )

        if not self._hooked:
            return False
        return True

    def _uninstallHookProc(self):
        if self._hooked is None:
            return
        user32.UnhookWindowsHookEx(self._hooked)
        self._hooked = None

    @abc.abstractmethod
    def _process_body(self, nCode, wParam, lParam):
        ...

    def _hookProc(self, nCode, wParam, lParam):
        self._process_body(nCode, wParam, lParam)
        return user32.CallNextHookEx(self._hooked, nCode, wParam, lParam)

    @staticmethod
    def _current_time():
        return int(datetime.datetime.now().timestamp())

    def _get_active_window_title(self):
        return self._wm.get_active_window().title

    @staticmethod
    def _callback(callback_):
        CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
        return CMPFUNC(callback_)

    def stop_listener(self):
        self._uninstallHookProc()
        process_id = kernel32.GetCurrentProcessId()
        handle = kernel32.OpenProcess(1, False, process_id)
        kernel32.TerminateProcess(handle, -1)
        kernel32.CloseHandle(handle)

    def start_listener(self):
        atexit.register(self._uninstallHookProc)
        self._installHookProc()
        msg = MSG()
        user32.GetMessageA(byref(msg), 0, 0, 0)
        user32.TranslateMessage(byref(msg))
        user32.DispatchMessageA(byref(msg))
