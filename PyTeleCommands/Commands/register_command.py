from functools import wraps

from ..CommandDict.command_dictionary import CommandDictionary
from ..Commands.command_base import CommandBase
from ..Errors import errors


class RegisterCommand:
    def __init__(self, command_name: str) -> None:
        CommandDictionary.set_command_name(command_name)

    def __call__(self, class_instance):
        if not issubclass(class_instance, CommandBase):
            raise errors.BadCommandStructure(class_instance, CommandBase)
        CommandDictionary.update_dictionary("class_instance", class_instance)
        return class_instance


class RegisterOption:
    _option_name: str

    def __init__(self, option_name: str) -> None:
        self.option_name = option_name

    @property
    def option_name(self) -> str:
        return self._option_name

    @option_name.setter
    def option_name(self, value: str) -> None:
        if not value.startswith("-"):
            self._option_name = "-" + value
        else:
            self._option_name = value

    def __call__(self, method_instance):
        CommandDictionary.update_dictionary(self._option_name, method_instance)

        @wraps(method_instance)
        def wrapper(*args, **kwargs):
            return method_instance(*args, **kwargs)

        return wrapper
