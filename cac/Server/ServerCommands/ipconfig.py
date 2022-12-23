from PyTeleCommands.Commands.command_base import CommandBase
from PyTeleCommands.Commands.register_command import RegisterCommand, RegisterOption


@RegisterCommand("ipconfig")  # command name in terminal
class IPConfig(CommandBase):
    def __init__(self):
        """ your code..."""

    @RegisterOption("-all")  # command option in terminal
    def option_all(self):
        """ your code..."""

    def execute(self):  # method executed as the latest
        """ your code..."""
