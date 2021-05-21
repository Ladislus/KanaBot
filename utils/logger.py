from datetime import datetime

_default = True


class Logger:
    def __init__(self, prefix: str, filepath: str = 'logs.txt', debug: bool = _default):
        self._prefix: str = prefix
        self._filepath: str = filepath
        self._debug: bool = debug

    def log(self, msg: str):
        with open(self._filepath, 'a') as file:
            file.write(f'({datetime.utcnow()})[{self._prefix}] {msg}\n')
        if self._debug:
            print(f'[{self._prefix}] {msg}')
