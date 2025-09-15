from __future__ import annotations
import abc
from typing import TypeVar, Generic


# 泛型型別
BrowserT = TypeVar('BrowserT')  # 瀏覽器
PageT = TypeVar('PageT')  # 頁面


class EngineInterface(abc.ABC):
    """爬蟲引擎介面"""

    @abc.abstractmethod
    async def __aenter__(self):
        """開啟異步上下文"""

    @abc.abstractmethod
    async def __aexit__(self, exc_type, exc_value, traceback):
        """關閉異步上下文"""


class BrowserInterface(abc.ABC):
    """瀏覽器"""

    @abc.abstractmethod
    async def launch(self, *args, **kws):
        """啟動"""

    @abc.abstractmethod
    async def close(self):
        """關閉"""

    @abc.abstractmethod
    async def new_page(self) -> PageInterface:
        """開啟頁面"""


class PageInterface(abc.ABC):
    """頁面"""

    @abc.abstractmethod
    async def goto(self, url: str, *args, **kws):
        """前往"""

    @abc.abstractmethod
    async def title(self):
        """取得頁面Title"""
