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
