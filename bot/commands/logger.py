from datetime import datetime


class Logger:
    def __init__(self, prefix: str, filepath: str = 'logs.txt'):
        self._prefix: str = prefix
        self._filepath: str = filepath

    def log(self, msg: str):
        with open(self._filepath, 'a') as file:
            file.write(f'({datetime.utcnow()})[{self._prefix}] {msg}\n')
