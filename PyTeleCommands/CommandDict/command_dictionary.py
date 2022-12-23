
class CommandDictionary:
    command_dict: dict = dict()
    command_name: str

    @classmethod
    def update_dictionary(cls, key, value) -> None:
        cls.command_dict.setdefault(cls.command_name, {}).update({key: value})

    @classmethod
    def set_command_name(cls, command_name: str) -> None:
        cls.command_name = command_name
