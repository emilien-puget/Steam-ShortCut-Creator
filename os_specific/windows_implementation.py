import os
import subprocess
import urllib.request
import zipfile
import sys

from . import os_specific_interface


class WindowsImplementation(os_specific_interface.OsSpecific):
    shortcut_folder = False
    location = False

    def __init__(self, location=None):
        print('Starting windows process')
        if not os.path.isfile(location + '\steam.exe'):
            print('Please place this file in the steam folder')
            sys.exit()
        self.location = location
        self.shortcut_folder = os.getenv('APPDATA') + '\Microsoft\Windows\Start Menu\Programs\Steam'
        if not os.path.isdir(self.shortcut_folder):
            os.mkdir(self.shortcut_folder)

    def download_steamcmd(self, path):
        steamcmd = path + '\steamcmd.exe'
        if os.path.isfile(steamcmd):
            return steamcmd

        print('Steamcmd is not found, downloading ...')
        archive = path + '\steamcmd.archive'
        try:
            urllib.request.urlretrieve('https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip',
                                       archive)
        except Exception as error:
            print('Steamcmd can\'t be downloaded : ' + error.__str__())
            return False

        zipfile.ZipFile(archive).extractall(path)

        os.remove(archive)
        if os.path.isfile(steamcmd):
            return steamcmd
        else:
            return False

    def create_shortcut(self, game):
        shortcut_file = self.shortcut_folder + "\\" + game['name'].replace(':', '') + '.lnk'

        if 'clienticon' in game and os.path.isfile(self.location + '\steam\games\\' + game['clienticon'] + '.ico'):
            clienticon = self.location + '\steam\games\\' + game['clienticon'] + '.ico'
        else:
            clienticon = self.location + '\Steam.exe'

        command = r'$shell = New-Object -comObject WScript.Shell ; ' \
                  r'$lnk = $shell.CreateShortcut("' + shortcut_file + '") ; ' \
                                                                      '$lnk.TargetPath = "' + self.location + '\steam.exe" ; $lnk.Arguments = "-applaunch ' + \
                  game['id'] + '" ; ' \
                               '$lnk.IconLocation="' + clienticon + '" ; $lnk.Save()'
        print('Creating shortcut for: ' + game['name'] + ' with icon: ' + clienticon)
        subprocess.Popen(['powershell.exe', command])

    @staticmethod
    def get_os_name():
        return 'windows'
