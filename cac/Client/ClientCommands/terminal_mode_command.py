from PyTeleCommands.Cli.terminal import TerminalModes
from PyTeleCommands.Commands.command_base import CommandBase
from PyTeleCommands.Commands.register_command import RegisterCommand, RegisterOption


@RegisterCommand("mode")  # command name in terminal
class TerminalModeCommand(CommandBase):

    def __init__(self):
        """ your code..."""

    @RegisterOption("-server")  # command option in terminal
    def option_server(self):
        from cac.Client.client_terminal import client_terminal as cl
        cl.set_terminal_mode(TerminalModes.server)
        return "Changed to server"

    @RegisterOption("-client")
    def option_client(self):
        from cac.Client.client_terminal import client_terminal as cl
        cl.set_terminal_mode(TerminalModes.server)
        return "Changed to client"

    def execute(self):  # method executed as the latest
        """ your code..."""
