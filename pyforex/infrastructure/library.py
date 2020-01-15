import os

from abc import ABC, abstractmethod
from ctypes import CDLL

import pyforex

class TelegramLibrary(ABC):

    @abstractmethod
    def load_library(self):
        """
            Return a Telegram 'tdjson' library.
            Used for a custom implementation depending on OS: OSX, Linux, Windows
        """
        pass


class TelegramLinuxLibrary(TelegramLibrary):

    def __init__(self):
        super().__init__()

    def load_library(self):
        try:
            tdjson = CDLL(os.path.join(pyforex.ROOT_DIR, "lib/libtdjson.so"))
            return tdjson
        except Exception as identifier:
            raise Exception("TelegramLinuxLibrary::Cannot load libtdjson.so", identifier)


class TelegramOSXLibrary(TelegramLibrary):

    def __init__(self):
        super().__init__()

    def load_library(self):
        try:
            tdlib_path = os.path.join(pyforex.ROOT_DIR, "lib/libtdjson.dylib")
            tdjson = CDLL(tdlib_path)
            return tdjson
        except Exception as identifier:
            raise Exception("TelegramOSXLibrary::Cannot load libtdjson.dylib", identifier)


class TelegramWindowsLibrary(TelegramLibrary):

    def __init__(self):
        super().__init__()

    def load_library(self):
        try:
            tdlib_path = os.path.join(pyforex.ROOT_DIR, "lib/tdjson32.dll")
            tdjson = CDLL(tdlib_path)
            return tdjson
        except:
            try:
                zlib_path = os.path.join(pyforex.ROOT_DIR, "lib/zlibd1.dll")
                CDLL(zlib_path)
                tdlib_path = os.path.join(pyforex.ROOT_DIR, "lib/tdjson64.dll")
                tdjson = CDLL(tdlib_path)
            except Exception as identifier:
                raise Exception("TelegramWindowsLibrary::Cannot load libtdjson(32|64).dll", identifier)
