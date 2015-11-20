import os
import urllib.request
import zipfile

import os_specific.os_specific_interface as os_specific_interface


class WindowsImplementation(os_specific_interface.OsSpecific):
    def download_steamcmd(self, path):
        if not os.path.isdir(path):
            os.mkdir(path)
        steamcmd = path + '/steamcmd.exe'
        if os.path.isfile(steamcmd):
            return steamcmd

        print('Steamcmd is not found, downloading ...')
        archive = path + '/steamcmd.archive'
        try:
            urllib.request.urlretrieve('https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip',
                                       archive)
        except Exception as error:
            print('steamcmd can\'t be downloaded : ' + error.__str__())
            exit()

        zipfile.ZipFile(archive).extractall(path)

        os.remove(archive)
        if os.path.isfile(steamcmd):
            return steamcmd
        else:
            return False

    def create_shortcut(self, game):
        pass

    def get_os_name(self):
        return 'windows'
