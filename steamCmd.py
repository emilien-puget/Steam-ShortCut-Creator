import re
import subprocess


class SteamCmd:
    def __init__(self, steam_cmd_path):
        self.steam_cmd_path = steam_cmd_path

    def get_installed_game(self):
        games = []
        for line in self._execute('apps_installed'):
            match = re.match("AppID (?P<id>\d+) : \"(?P<name>[^`\"]*)\" : (?P<path>.+) ", line)
            if match:
                game = {'id': match.group('id'), 'name': match.group('name'), 'path': match.group('path')}
                games.insert(0, game)

        return games

    def get_app_icons(self, id_game):
        game_icon = {}

        for line in self._execute('app_info_print ' + str(int(id_game))):
            match = re.match(
                "(^.*\"clienticon\".*\"(?P<clienticon>[0-9a-z]+)\")"
                "|(^.*\"linuxclienticon\".*\"(?P<linuxclienticon>[0-9a-z]+)\")",
                line)
            if match:
                if match.group('clienticon'):
                    game_icon['clienticon'] = match.group('clienticon')
                if match.group('linuxclienticon'):
                    game_icon['linuxclienticon'] = match.group('linuxclienticon')

        return game_icon

    def _execute(self, function_name):
        command = self.steam_cmd_path + ' +' + function_name

        for x in range(0, 50):
            command += ' +app_info_print 0 '
        command += ' +quit'

        return subprocess.getoutput(command).splitlines()
