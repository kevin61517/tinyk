from __future__ import annotations
import abc
from typing import Generic, TypeVar
from contextlib import AbstractAsyncContextManager


EngineT = TypeVar('EngineT')


class EngineInterface(abc.ABC, Generic[EngineT]):
    """爬蟲引擎介面"""

    @abc.abstractmethod
    def __init__(self, *args, **kws):
        """初始化"""

    @abc.abstractmethod
    async def init_engine(self, *args, **kws) -> EngineT:
        """
        功能：基類設置引擎物件。
        說明：調用或回傳引擎啟動入口(Selenium, Pyppeteer, Playwright)。
        """

    @abc.abstractmethod
    def use_engine(self, name) -> EngineInterface:
        """選擇引擎"""

    @abc.abstractmethod
    async def init_browser(self, name: str) -> BrowserInterface:
        """
        功能：取得瀏覽器。
        說明：在engine被賦值後，根據 name 參數來回傳不同引擎的不同瀏覽器實例。
        """


class BrowserInterface(AbstractAsyncContextManager, abc.ABC):
    """瀏覽器介面"""

    @abc.abstractmethod
    async def __aenter__(self):
        """開啟上下文"""

    @abc.abstractmethod
    async def __aexit__(self, exc_type, exc_value, traceback):
        """關閉上下文"""

    @abc.abstractmethod
    async def launch(self, *args, **kws) -> BrowserInterface:
        """
        功能：啟動瀏覽器。
        說明：啟動瀏覽器具體實作。
        """

    @abc.abstractmethod
    async def close(self):
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
