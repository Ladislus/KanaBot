from .commandfunctions import test, enculai, ladislas
from .commandoptions import Option
from .commandelement import Element

commandlist: dict = {
    'test': {
        Option.ARGUMENT_REQUIRED: 0,
        Option.ELEMENT_REQUIRED: [Element.CHANNEL],
        Option.VARARGS_SUPPORTED: False,
        Option.NAMED_ARGUMENTS: [],
        Option.FUNCTION: test
    },
    'enculai': {
        Option.ARGUMENT_REQUIRED: 0,
        Option.ELEMENT_REQUIRED: [Element.CHANNEL, Element.USERS],
        Option.VARARGS_SUPPORTED: False,
        Option.NAMED_ARGUMENTS: [],
        Option.FUNCTION: enculai
    },
    'ladislas': {
        Option.ARGUMENT_REQUIRED: 0,
        Option.ELEMENT_REQUIRED: [Element.CHANNEL],
        Option.VARARGS_SUPPORTED: False,
        Option.NAMED_ARGUMENTS: [],
        Option.FUNCTION: ladislas
    }
}
