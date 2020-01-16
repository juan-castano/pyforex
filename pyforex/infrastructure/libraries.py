import os

from abc import ABC, abstractmethod
from ctypes import CDLL

import pyforex
from pyforex.loaders import signature_telegram_library

from pyforex.infrastructure.enums import LibraryName

class TelegramLibrary(ABC):

    @abstractmethod
    def load_library(self) -> CDLL:
        """
            Return a Telegram 'tdjson' library.
            Used for a custom implementation depending on OS: OSX, Linux, Windows
        """
        pass

    def generate_definitions(self):
        pass


class TelegramLinuxLibrary(TelegramLibrary):

    def __init__(self):
        super().__init__()

    def load_library(self) -> CDLL:
        try:
            tdjson = CDLL(os.path.join(pyforex.LIB_DIR, LibraryName.LINUX.value))
            return signature_telegram_library(tdjson)
        except Exception as identifier:
            raise Exception("TelegramLinuxLibrary::Cannot load libtdjson.so", identifier)


class TelegramOSXLibrary(TelegramLibrary):

    def __init__(self):
        super().__init__()

    def load_library(self) -> CDLL:
        try:
            tdlib_path = os.path.join(pyforex.LIB_DIR, LibraryName.OSX.value)
            tdjson = CDLL(tdlib_path)
            return signature_telegram_library(tdjson)
        except Exception as identifier:
            raise Exception("TelegramOSXLibrary::Cannot load libtdjson.dylib", identifier)


class TelegramWindowsLibrary(TelegramLibrary):

    def __init__(self):
        super().__init__()

    def load_library(self) -> CDLL:
        try:
            tdlib_path = os.path.join(pyforex.LIB_DIR, LibraryName.WIN32.value)
            tdjson = CDLL(tdlib_path)
            return signature_telegram_library(tdjson)
        except:
            try:
                zlib_path = os.path.join(pyforex.LIB_DIR, LibraryName.WIN64_ZLIB.value)
                CDLL(zlib_path)
                tdlib_path = os.path.join(pyforex.LIB_DIR, LibraryName.WIN64.value)
                tdjson = CDLL(tdlib_path)
                return signature_telegram_library(tdjson)
            except Exception as identifier:
                raise Exception("TelegramWindowsLibrary::Cannot load libtdjson(32|64).dll", identifier)
