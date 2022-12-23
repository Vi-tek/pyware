from PyTeleCommands.Commands.command_base import CommandBase
from PyTeleCommands.Commands.register_command import RegisterCommand, RegisterOption


@RegisterCommand("ping")  # command name in terminal
class Ping(CommandBase):
    def __init__(self):
        """ your code..."""

    @RegisterOption("-ip")  # command option in terminal
    def option_ip(self, ip_address):
        """ your code..."""
        return ip_address

    @RegisterOption("-ttl")
    def option_ttl(self):
        """your code..."""

    def execute(self):  # method executed as the latest
        """ your code..."""
        return "pong"

