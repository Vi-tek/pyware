class TerminalCommand:
    name: str = ""
    options: dict
    name_error: str = ""
    option_error: str = ""
    __char_range: range = range(97, 123)

    @classmethod
    def __set_command_name(cls, array: list[str]):
        command_name = array.pop(0).lower()
        if ord(command_name[0]) in cls.__char_range:
            cls.name = command_name
        else:
            cls.name_error = command_name

    @classmethod
    def __set_command_options(cls, array: list[str]):
        cls.options = dict()
        option_identifier = ""
        for item in array:
            try:
                if item.startswith("-"):
                    option_identifier = item
                    cls.options[option_identifier] = ""
                else:
                    cls.options[option_identifier] = [*cls.options[option_identifier], item]
            except KeyError:
                cls.option_error = item
                return None

    @classmethod
    def from_list(cls, array: list[str]):
        cls.__set_command_name(array)
        cls.__set_command_options(array)
        return cls
