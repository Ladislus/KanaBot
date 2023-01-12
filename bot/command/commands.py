from time import time


from utils import ExitCode
from .registerer import register, COMMAND_SET
from .command import Command

_start_time: time = time()


@register(
    name='help',
    description='Print bot command list')
async def _help(command: Command) -> bool:
    msg: str = ''
    for name, command_info in COMMAND_SET.items():
        msg += f'\t*{name}* :\n\t\t{command_info.description}\n'
    await command.channel.send(f'**Command list:**\n{msg}')
    return True


@register(
    name='uptime',
    description='Get bot uptime')
async def _uptime(command: Command) -> bool:
    await command.channel.send(f'uptime: {int(time() - _start_time)}s')
    return True


@register(
    name='kill',
    description='Kill Billy',
    admin_required=True)
async def _kill(command: Command):
    await command.channel.send(f'Adieu monde cruel !\nhttps://giphy.com/gifs/studiosoriginals-bye-byebye-3o7btQsLqXMJAPu6Na')
    command.logger.log("Exit command")
    exit(ExitCode.KILL_COMMAND)
