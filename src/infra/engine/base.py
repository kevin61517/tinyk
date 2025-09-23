from __future__ import annotations
import abc
from typing import TypeVar, Generic, Type, Union, Protocol
from src.domain.engine import EngineInterface, BrowserInterface, PageInterface, EngineT, LauncherT, BrowserT
from src.domain.registry import RegisterInterface, RegistrableInterface


PageT = TypeVar('PageT')
EngineName = str


class EngineRegister(RegisterInterface[Type[EngineInterface]]):
    """引擎註冊器"""

    def get(self, name: str):
        """取得被註冊的物件"""
        cls = self._registry.get(name.lower())
        if not cls:
            raise TypeError(f'Engine "{name}" not implement.')
        return cls

    def register(self, cls: Type[Union[RegistrableInterface, EngineInterface]], **kws):
        """
        功能：註冊
        說明：
         - cls：引擎類。
         - launcher：爬蟲套件啟動入口。
        """
        name = cls.get_name()
        if self._registry.get(name.lower()) is not None:
            raise TypeError(f'Engine "{name}" implemented already, please change name or change engine implementation.')
        self._registry[name.lower()] = cls

    @property
    def registries(self):
        """枚舉註冊物件"""
        for name, cls in self._registry.items():
            yield name, cls


class BaseEngine(EngineInterface[EngineT, BrowserT], RegistrableInterface, abc.ABC):
    """引擎基類"""


class BaseBrowser(BrowserInterface[LauncherT, BrowserT], RegistrableInterface, abc.ABC):
    """瀏覽器基類"""


class BasePage(PageInterface, abc.ABC, Generic[PageT]):

    def __init__(self, page: PageT):
        self._page = page
