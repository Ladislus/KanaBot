from env import OWNER
from config.globalconfig import GlobalConfig
from discord import Message
from discord.abc import User


def is_owner(u: User) -> bool:
    return OWNER == f'{u.name}#{u.discriminator}'


def is_command(msg: str) -> bool:
    return msg.lstrip()[0] == '!'


def validate(msg: Message, globalCfg: GlobalConfig) -> bool:
    return globalCfg.activated and \
           is_command(msg.content) and \
           msg.channel.name in globalCfg.channels and \
           (not globalCfg.adminRequired or (msg.author.id in globalCfg.admins or is_owner(msg.author)))
