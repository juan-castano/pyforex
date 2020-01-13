from pyforex.domain.telegram_domain import TelegramDomain

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

print("::: PYFOREX :::")
print(">>> Working on {}".format(ROOT_DIR))


def app_run():
    telegram_domain = TelegramDomain()
    telegram_domain.verify_manager()