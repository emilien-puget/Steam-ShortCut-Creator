import steamCmd
import os
import configparser

if os.path.isfile('settings.cfg'):
    parser = configparser.ConfigParser()
    parser.read('settings.cfg')

    steam_cmd_path = parser.get('parameters', 'steam_cmd_path')
    path = os.path.dirname(__file__) + '/' + steam_cmd_path
    if os.path.isfile(path):
        steam = steamCmd.SteamCmd(path)
        steam.get_installed_game()
    else:
        print("Can't find steamCmd at '" + path + "'")
else:
    exit()
