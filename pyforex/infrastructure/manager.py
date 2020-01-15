import sys

from pyforex.infrastructure.enums import OSEnum
from pyforex.infrastructure.library import \
    TelegramLibrary, TelegramLinuxLibrary, TelegramOSXLibrary, TelegramWindowsLibrary

class TelegramManagerLibrary(object):

    def __init__(self):
        super().__init__()
        self.__load_manager()

    def __load_manager(self):
        os_name = sys.platform

        if os_name == OSEnum.OSX.value:
            telegramOSXLibrary = TelegramOSXLibrary()
            self.__manager = telegramOSXLibrary.load_library()
        elif os_name == OSEnum.LINUX.value:
            telegramLinuxLibrary = TelegramLinuxLibrary()
            self.__manager = telegramLinuxLibrary.load_library()
        elif os_name == OSEnum.WIN.value:
            telegramWindowsLibrary = TelegramWindowsLibrary()
            self.__manager = telegramWindowsLibrary.load_library()
        else:
            raise Exception("Not implemented yet: {}".format(sys.platform))

    def get_manager(self) -> TelegramLibrary:
        return self.__manager
