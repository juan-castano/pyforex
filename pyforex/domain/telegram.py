import json

from pyforex.infrastructure.managers import TelegramManagerLibrary

class TelegramDomain(object):

    def __init__(self):
        super().__init__()
        self.__manager = TelegramManagerLibrary().get_manager()
        self.verify_manager()

    def verify_manager(self):
        if self.__manager == None:
            print("TelegramDomain None", self.__manager)
        else:
            print("TelegramDomain Alive", self.__manager)

    def get_manager(self) -> TelegramManagerLibrary:
        return self.__manager

    """def client_create(self):
        self.__manager.td_json_client_create
        tdjson.td_json_client_create"""


class TelegramClient(object):

    def __init__(self, manager: TelegramDomain):
        self.__manager = manager

    def create(self):
        self.__client = self.__manager.get_manager().td_json_client_create()

    def send(self, query):
        query_result = json.dumps(query).encode('utf-8')
        self.__manager.get_manager().td_json_client_send(self.__client, query_result)

    def receive(self):
        result = self.__manager.get_manager().td_json_client_receive(self.__client, 1.0)
        if result:
            result = json.loads(result.decode('utf-8'))
        return result
