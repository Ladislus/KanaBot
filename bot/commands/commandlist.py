from .commandfunctions import test
from .commandoptions import Option

commandlist: dict = {
    'test': {
        Option.ARGUMENT_REQUIRED: 0,
        Option.VARARGS_SUPPORTED: False,
        Option.NAMED_ARGUMENTS: [],
        Option.FUNCTION: test
    }
}
