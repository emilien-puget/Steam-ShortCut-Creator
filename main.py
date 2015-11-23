import os
import platform

import steamCmd
import os_specific.os_specific_interface as os_specific_interface
import os_specific.linux_implementation
import os_specific.windows_implementation
import os_specific.os_specific_factory as os_specific_factory

OsSpecificFactory = os_specific_factory.OsSpecificFactory()
osSpecificImplementation = OsSpecificFactory.create(platform.system())(os.getcwd())
if not issubclass(osSpecificImplementation.__class__, os_specific_interface.OsSpecific):
    print('No implementation found for ' + platform.system())
    exit()

steam_cmd_path = osSpecificImplementation.download_steamcmd(os.getcwd())
if not steam_cmd_path or not os.path.isfile(steam_cmd_path):
    exit()

steam = steamCmd.SteamCmd(steam_cmd_path)
print('Fetching installed applications')
games = steam.get_installed_game()
if len(games) > 0:
    print(str(len(games)) + " application" + ("s" if len(games) > 0 else "") + " found")

    for game in games:
        game.update(steam.get_app_icons(game['id']))
        osSpecificImplementation.create_shortcut(game)
    print('Finishing')
else:
    print('No application found')
