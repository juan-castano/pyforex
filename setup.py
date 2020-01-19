import pyforex
import threading

from pyforex.app.app import TelegramApp

if __name__ == "__main__":
    telegram_app = TelegramApp()
    threading.Thread(target=telegram_app.run()).start()
    #pyforex.app_run()