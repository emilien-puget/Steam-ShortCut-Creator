import os
import re
import tarfile
import urllib.request

from . import os_specific_interface


class LinuxImplementation(os_specific_interface.OsSpecific):
    shortcut_folder = False

    def __init__(self, location):
        print('Starting linux process')
        user_home_directory = os.path.expanduser("~")
        for path in os.environ["PATH"].split(os.pathsep):
            if path[0:len(user_home_directory)] == user_home_directory and os.access(path, os.W_OK):
                self.shortcut_folder = path
                print('Shortcuts will be created in ' + self.shortcut_folder)
                break

        if not self.shortcut_folder:
            print('No folder found for the shortcuts, creating one')
            steamlnk_shortcuts_directory = user_home_directory + '/.steamlnk_shortcuts'
            if not os.path.isdir(steamlnk_shortcuts_directory):
                os.mkdir(steamlnk_shortcuts_directory)

            self.shortcut_folder = steamlnk_shortcuts_directory

    def download_steamcmd(self, path):
        path += '/steamcmd_client'
        if not os.path.isdir(path):
            os.mkdir(path)
        steamcmd = path + '/steamcmd.sh'
        if os.path.isfile(steamcmd):
            return steamcmd

        print('Steamcmd is not found, downloading ...')
        archive = path + '/steamcmd.archive'
        try:
            urllib.request.urlretrieve('https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz',
                                       archive)
        except Exception as error:
            print('Steamcmd can\'t be downloaded : ' + error.__str__())
            exit()

        tar = tarfile.open(archive)
        tar.extractall(path)
        tar.close()
        os.remove(archive)

        if os.path.isfile(steamcmd):
            return steamcmd
        else:
            return False

    def create_shortcut(self, game):
        bin_shortcut = self.shortcut_folder + '/' + game['name']
        print('Creating shortcut for: ' + game['name'] + ' in: ' + bin_shortcut)

        handle = os.fdopen(os.open(bin_shortcut, os.O_WRONLY | os.O_CREAT, int("0777", 8)), 'w')

        handle.write('steam -applaunch ' + game['id'])

    @staticmethod
    def get_os_name():
        return 'linux'
