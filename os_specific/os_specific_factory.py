from . import os_specific_interface


class OsSpecificFactory:
    subclass = {}

    def __init__(self):
        for implementation in os_specific_interface.OsSpecific.__subclasses__():
            self.subclass[implementation.get_os_name()] = implementation

    def create(self, name):
        if self.subclass.__contains__(name.lower()):
            return self.subclass.get(name.lower())
