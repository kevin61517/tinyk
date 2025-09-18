from __future__ import annotations
import abc
from typing import Optional, TypeVar, Generic, Dict, Type
from src.domain.engine import EngineInterface, BrowserInterface, PageInterface, EngineT
from src.domain.registry import RegisterInterface, RegistrableInterface


BrowserT = TypeVar('BrowserT')
PageT = TypeVar('PageT')
EngineName = str


class EngineRegister(RegisterInterface[EngineInterface]):
    """引擎註冊器"""

    def get(self, name: str):
        """取得被註冊的物件"""
        cls = self._registry.get(name.lower())
        if not cls:
            raise TypeError(f'Engine "{name}" not implement.')
        return cls

    def register(self, cls):
        """註冊"""
        name = cls.get_name()
        if self._registry.get(name.lower()) is not None:
            raise TypeError(f'Engine "{name}" implemented already, please change name or change engine implementation.')
        self._registry[name.lower()] = cls

    @property
    def registries(self):
        """枚舉註冊物件"""
        for name, cls in self._registry.items():
            yield name, cls


class BaseEngine(EngineInterface[EngineT], RegistrableInterface, abc.ABC):

    def __init__(self, *args, **kws):
        """初始化引擎"""
        self._engine: Optional[EngineT] = None
        self._args = args
        self._kws = kws

    async def init_engine(self) -> EngineInterface[EngineT]:
        """初始化引擎"""
        self._engine = await self._init(*self._args, **self._kws)
        return self

    @abc.abstractmethod
    async def _init(self, *args, **kws):
        """初始化引擎實作"""

    async def init_browser(self, name: str) -> BrowserInterface:
        """初始化瀏覽器"""
        return await self._init_browser(name.lower())

    @abc.abstractmethod
    async def _init_browser(self, name) -> BrowserInterface:
        """初始化瀏覽器實作"""


class BaseBrowser(BrowserInterface, abc.ABC, Generic[BrowserT]):

    def __init__(self, browser: Optional[BrowserT], *args, **kws):
        self._browser: BrowserT = browser
        self._launched = False

    async def __aenter__(self):
        """開啟上下文"""
        if self._is_launched():
            return self
        raise Exception('Use async with instance.launch(...) to start browser.')

    async def __aexit__(self, exc_type, exc_value, traceback):
        """關閉上下文"""
        await self.close()
        self._launch_off()

    async def launch(self, *args, **kws) -> BrowserInterface:
        """開啟瀏覽器資源"""
        try:
            await self._init_browser(*args, **kws)
            self._launch_on()
            return self
        except Exception as e:
            self._launch_off()
            raise e

    @abc.abstractmethod
    async def _init_browser(self, *args, **kws):
        """
        功能：初始化瀏覽器。
        說明：根據不同引擎實作不同的初始化過程。
        """

    async def close(self):
        """關閉瀏覽器資源"""
        try:
            await self._shutdown_browser()
            self._launch_off()
        except Exception as e:
            raise e

    @abc.abstractmethod
    async def _shutdown_browser(self):
        """
        功能：釋放瀏覽器資源。
        說明：根據不同引擎實作不同的釋放過程。
        """

    def _launch_on(self):
        if self._is_launched():
            raise Exception('Browser launched currently.')
        self._launched = True

    def _launch_off(self):
        self._launched = False

    def _is_launched(self):
        return self._launched


class BasePage(PageInterface, abc.ABC, Generic[PageT]):

    def __init__(self, page: PageT):
        self._page = page
