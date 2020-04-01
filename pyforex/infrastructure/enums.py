from enum import Enum

class OSEnum(Enum):
    OSX = 'darwin'
    WIN = 'win32'
    LINUX = 'linux'

    def __str__(self):
        return "{}".format(self.value)


class LibraryName(Enum):
    OSX = 'libtdjson.dylib'
    WIN32 = 'tdjson32.dll'
    WIN64_ZLIB = 'zlibd1.dll'
    WIN64 = 'tdjson64.dll'
    LINUX = 'libtdjson.so'
