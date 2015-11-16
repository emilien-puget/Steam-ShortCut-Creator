import re
import subprocess


class SteamCmd:
    def __init__(self, steam_cmd_path):
        self.steam_cmd_path = steam_cmd_path

    def get_installed_game(self):
        self._execute('apps_installed')

    def _execute(self, function_name):
        command = self.steam_cmd_path + ' +' + function_name + ' +quit'

        output = subprocess.check_output(command.split())

        output_splited = output.splitlines()
        for line in output_splited:

            print(line)

