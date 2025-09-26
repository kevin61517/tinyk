from __future__ import annotations
import abc
from typing import Generic, TypeVar
from contextlib import AbstractAsyncContextManager


LauncherT = TypeVar('LauncherT')
BrowserT = TypeVar('BrowserT')


class EngineInterface(abc.ABC, Generic[BrowserT]):
    """爬蟲引擎介面"""

    @classmethod
    @abc.abstractmethod
    async def launch(cls, **options) -> EngineInterface:
        """
        功能：啟動引擎。
        說明：根據不同引擎實作啟動。
        """

    @abc.abstractmethod
    async def shutdown(self, **kws) -> None:
        """
        功能：關閉引擎。
        說明：根據不同引擎實作關閉。
        :return:
        """

    @abc.abstractmethod
    def get_browser(self, name: str) -> BrowserT:
        """
        功能：取得瀏覽器。
        說明：根據不同引擎實作取得瀏覽器。
        """


class BrowserInterface(AbstractAsyncContextManager, abc.ABC, Generic[LauncherT, BrowserT]):
    """瀏覽器介面"""

    def __init__(self, launcher: LauncherT, **options):
        self._launcher: LauncherT = launcher
        self._options = options
        self._browser: BrowserT = None

    async def __aenter__(self):
        """開啟上下文"""
        try:
            await self._launch()
            return self
        except Exception as e:
            await self._shutdown()
            raise e

    async def __aexit__(self, exc_type, exc_value, traceback):
        """關閉上下文"""
        try:
            await self._shutdown()
        except Exception as e:
            raise e

    @abc.abstractmethod
    async def _launch(self) -> BrowserInterface:
        """
        功能：啟動瀏覽器。
        說明：啟動瀏覽器具體實作。
        """

    @abc.abstractmethod
    async def _shutdown(self):
        """
        功能：關閉瀏覽器。
        說明：關閉瀏覽器具體實作。
        """

    @abc.abstractmethod
    async def new_page(self, *args, **kws) -> PageInterface:
        """
        功能：開啟頁面。
        說明：根據不同引擎實作不同的開啟頁面方式。
        """


class PageInterface(abc.ABC):
    """頁面介面"""

    @abc.abstractmethod
    async def goto(self, url: str, *args, **kws):
        """前往"""

    @abc.abstractmethod
    async def title(self, *args, **kws):
        """取得頁面Title"""
