import abc


class OsSpecific:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def download_steamcmd(self, path):
        pass

    @abc.abstractmethod
    def create_shortcut(self, game):
        pass

    @abc.abstractmethod
    def get_os_name(self):
        pass
