import enum

class JSONTypes(enum.Enum):
    NUMBER = 1
    STRING = 2
    BOOLEAN = 3
    ARRAY = 4
    OBJECT = 5
    NULL = 6
    INVALID = 7