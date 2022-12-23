from ..Prefixes.prefix import Prefix


class BaseErrorHandler(Exception):
    def __init__(self, message: str):
        super(BaseErrorHandler, self).__init__(message)
        self.message = message

    def to_string(self):
        return Prefix.error + self.message


class BadCommandStructure(BaseErrorHandler):
    def __init__(self, class_instance, super_class):
        super(BadCommandStructure, self).__init__(f"Class {class_instance} must derive from {super_class}")


class CommandDoesNotExistError(BaseErrorHandler):
    def __init__(self, command_name: str):
        super(CommandDoesNotExistError, self).__init__(f"Command [{command_name}] does not exist")


class OptionDoesNotExistError(BaseErrorHandler):
    def __init__(self, option):
        super(OptionDoesNotExistError, self).__init__(f"Option [{option}] does not exist")


class NoCommandOptionSetError(BaseErrorHandler):
    def __init__(self):
        super(NoCommandOptionSetError, self).__init__(f"Command name should be followed by an option not an argument")


class BadCommandNameError(BaseErrorHandler):
    def __init__(self):
        super(BadCommandNameError, self).__init__(f"Command should start from a-z")


class BadNumberOfArgumentsError(BaseErrorHandler):
    def __init__(self, message, option, args: list):
        super(BadNumberOfArgumentsError, self).__init__(f"{message} [{option}] args: [{','.join(args)}]")
