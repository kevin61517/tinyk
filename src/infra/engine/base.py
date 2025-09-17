from __future__ import annotations
import abc
from typing import Optional, TypeVar, Generic, Dict, Type
from src.domain.engine import EngineInterface, BrowserInterface


EngineT = TypeVar('EngineT')
BrowserT = TypeVar('BrowserT')
EngineName = str


class BaseEngine(EngineInterface, abc.ABC):

    _registry: Dict[EngineName, Type[EngineInterface]] = {}
    __Engine__ = None  # 設置引擎(Selenium, Pyppeteer, PlayWrite)

    def __init_subclass__(cls, name: EngineName = None, **kws):
        """Subclass Hook"""
        # 檢查屬性實作
        if cls.__Engine__ is None:
            raise TypeError('Attribute __Engine__ must have a reference.')

        # 檢查重複實作
        key, value = name.lower() or cls.__name__.lower(), cls
        if cls._registry.get(key) is not None:
            raise TypeError(f'Engine "{key}" implemented already, please change name or change Engine.')
        cls._registry[key] = cls

    def __init__(self):
        """初始化引擎"""
        self._engine = self.__Engine__

    def use_engine(self, key: EngineName) -> Type[EngineInterface]:
        """選擇引擎"""
        engine = self._registry.get(key, None)
        if engine is None:
            raise TypeError(f'Engine "{key}" not implemented')
        return engine


class BaseBrowser(BrowserInterface, abc.ABC, Generic[BrowserT]):

    def __init__(self, browser: BrowserT):
        self._browser: Optional[BrowserT] = browser
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

    async def launch(self, *args, **kws):
        """開啟瀏覽器資源"""
        try:
            await self._init_browser(*args, **kws)
            self._launch_on()
        except Exception as e:
            self._launch_off()
            raise e
        return self

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
        if not self._is_launched():
            self._launched = True
        raise Exception('Browser launched currently.')

    def _launch_off(self):
        self._launched = False

    def _is_launched(self):
        return self._launched


class Page:
    ...