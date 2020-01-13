from pyforex.infrastructure.manager import TelegramManagerLibrary

class TelegramDomain(object):

    def __init__(self):
        super().__init__()
        manager = TelegramManagerLibrary()
        self.__manager = manager.get_manager()

    def verify_manager(self):
        if self.__manager == None:
            print("TelegramDomain None", self.__manager)
        else:
            print("TelegramDomain Alive", self.__manager)