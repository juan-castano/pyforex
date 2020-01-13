from enum import Enum

class OSEnum(Enum):
    OSX = 'darwin'
    WIN = 'win32'
    LINUX = 'linux'

    def __str__(self):
        return "{}".format(self.value)
