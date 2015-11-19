import configparser
import os
import steamCmd

if os.path.isfile('settings.cfg'):
    parser = configparser.ConfigParser()
    parser.read('settings.cfg')

    steam_cmd_path = parser.get('parameters', 'steam_cmd_path')
    path = os.path.dirname(__file__) + '/' + steam_cmd_path
    if os.path.isfile(path):
        steam = steamCmd.SteamCmd(path)
        games = steam.get_installed_game()
        if len(games) > 0:
            for game in games:
                game.update(steam.get_app_icons(game['id']))
            print(str(len(games)) + " game" + ("s" if len(games) > 0 else "") + " found")
            print(games)
        else:
            print('no game found')
    else:
        print("Can't find steamCmd at '" + path + "'")
else:
    exit()
