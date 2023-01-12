from sys import stdout, stderr
from datetime import datetime

LOGGER_DEBUG_DEFAULT: bool = True


class Logger:
    def __init__(self, prefix: str, filepath: str = './logs.txt', debug: bool = LOGGER_DEBUG_DEFAULT):
        self._prefix: str = prefix
        self._filepath: str = filepath
        self._debug: bool = debug

    def _file_print(self, level: str, message: str, time: datetime = datetime.utcnow()):
        with open(self._filepath, 'a') as file:
            file.write(f'<{level}> ({time}) [{self._prefix}] {message}\n')

    def _console_print(self, message: str, file=stdout):
        if self._debug:
            print(f'[{self._prefix}] {message}', file=file)

    def log(self, message: str):
        self._file_print('LOG', message)
        self._console_print(message)

    def debug(self, message: str):
        self._console_print(message)

    def error(self, message: str):
        self._file_print('ERROR', message)
        self._console_print(message, stderr)
