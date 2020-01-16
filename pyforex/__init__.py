from pyforex.domain.telegram import TelegramDomain

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_DIR = os.path.join(ROOT_DIR, "lib")

print("::: PYFOREX :::")
print(">>> Working on {}".format(ROOT_DIR))


def app_run():
    telegram_domain = TelegramDomain()
    telegram_domain.verify_manager()