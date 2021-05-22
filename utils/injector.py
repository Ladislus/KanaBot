from typing import Optional
from config import GlobalConfig


class Injector:
    _cfg: Optional[GlobalConfig] = None

    @staticmethod
    def saveConfig(cfg: GlobalConfig) -> None:
        Injector._cfg = cfg

    @staticmethod
    def getConfig() -> Optional[GlobalConfig]:
        return Injector._cfg
