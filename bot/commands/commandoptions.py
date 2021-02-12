from enum import Enum, auto


class Option(Enum):
    ARGUMENT_REQUIRED = auto()
    ELEMENT_REQUIRED = auto()
    VARARGS_SUPPORTED = auto()
    NAMED_ARGUMENTS = auto()
    FUNCTION = auto()


