def parser(com: list[str]) -> dict:
    return {}


class Command:
    def __init__(self, msg: str):
        com: list[str] = msg.split(' ')
        self._name = com[0][1:]
        self._args = parser(com[1:])

    def __repr__(self) -> str:
        return f'Command: \n\
            \tName: {self._name}\n\
            \tArgs: {self._args}\n'
