import os
import platform

import steamCmd
from os_specific import *

OsSpecificFactory = os_specific_factory.OsSpecificFactory()
osSpecificImplementation = OsSpecificFactory.create(platform.system())()

if not issubclass(osSpecificImplementation.__class__, os_specific_interface.OsSpecific):
    print('No implementation found for ' + platform.system())
    exit()

print('Looking for steamcmd')
steam_cmd_path = osSpecificImplementation.download_steamcmd(os.path.dirname(__file__) + '/steamcmd')
if not steam_cmd_path or not os.path.isfile(steam_cmd_path):
    exit()

steam = steamCmd.SteamCmd(steam_cmd_path)
print('Fetching installed applications')
games = steam.get_installed_game()
if len(games) > 0:
    print(str(len(games)) + " application" + ("s" if len(games) > 0 else "") + " found")

    for game in games:
        osSpecificImplementation.create_shortcut(steam.get_app_icons(game['id']))
else:
    print('No application found')
