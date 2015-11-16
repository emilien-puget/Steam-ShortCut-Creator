import steamCmd
import os
import configparser

if os.path.isfile('settings.cfg'):
    parser = configparser.ConfigParser()
    parser.read('settings.cfg')

    steam_cmd_path = parser.get('parameters', 'steam_cmd_path')

    print(os.path.dirname(__file__))
    steam = steamCmd.SteamCmd(os.path.dirname(__file__) + '/' + steam_cmd_path)
    steam.get_installed_game()
else:
    exit()
