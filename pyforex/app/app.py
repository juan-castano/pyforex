import json
from abc import ABC, abstractmethod

from pyforex.domain.telegram import TelegramClient, TelegramDomain


class App(ABC):

    @abstractmethod
    def run(self):
        pass


class TelegramApp(App):
    
    def __init__(self):
        # super().__init__()
        telegram_manager = TelegramDomain()
        self.__telegram_client = TelegramClient(telegram_manager)
        self.__telegram_client.create()

    def run(self):        
        while True:
            event = self.__telegram_client.receive()
            if event:
                if event.get('@type') == 'updateAuthorizationState':
                    authtype = event.get('authorization_state').get('@type')
                    if authtype == "authorizationStateWaitTdlibParameters":
                        self.__telegram_client.send({'@type': 'setTdlibParameters',
                            'parameters': {'use_test_dc': False,
                                            'api_id':94575,
                                            'api_hash': 'a3406de8d171bb422bb6ddf3bbd800e2',
                                            'device_model': 'Desktop',
                                            'system_version': 'Unknown',
                                            'application_version': "0.0",
                                            'system_language_code': 'en',
                                            'database_directory': 'Database',
                                            'files_directory': 'Files',
                                            'use_file_database': True,
                                            'use_chat_info_database': True,
                                            'use_message_database': True,
                                            }
                            })
                    elif authtype == 'authorizationStateWaitEncryptionKey':
                        self.__telegram_client.send({'@type': 'checkDatabaseEncryptionKey', 'encryption_key': 'randomencryption'})
                    elif authtype == "authorizationStateWaitPhoneNumber":
                        phone = input('Enter phone number:')
                        self.__telegram_client.send({'@type': 'setAuthenticationPhoneNumber',
                                'phone_number': str(phone),
                                'allow_flash_call': False,
                                'is_current_phone_number': False}
                                )
                    elif authtype == "authorizationStateWaitCode":
                        code = input('Enter code:')
                        self.__telegram_client.send({'@type': 'checkAuthenticationCode', 'code': str(code)})
                    elif authtype == "authorizationStateWaitPassword":
                        password = getpass.getpass('Password:')
                        self.__telegram_client.send({'@type': 'checkAuthenticationPassword', 'password': password})
                    elif authtype == "authorizationStateReady":
                        print('Established connection')
                if event.get('@type') == 'updateChatReadInbox':
                    print('UpdateChatReadInbox: {}'.format(event))

                if event.get('@type') == 'updateNewMessage':
                    message = event.get('message')
                    if message.get('is_channel_post'):
                        print(message.get('content'))
                
                if event.get('@type') == 'updateChatLastMessage':
                    #last_message = json.loads(event.get('@type'))
                    #if last_message.get('@type') == 'message':
                    #print(json.dumps(last_message.get('message').encode('utf-8')))
                    pass
                    
                if event.get('@type') == 'updateSupergroup':
                    print('Supergroup')

                if event.get('@type') == 'updateSupergroupFullInfo':
                    print('Supergroup info')
