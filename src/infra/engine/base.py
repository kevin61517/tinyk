import abc
from src.domain.engine import EngineInterface


class Engine(EngineInterface):
    """
    爬蟲引擎
     - 瀏覽器
     - 頁面
    """
    def __init__(self):
        self._browser = None
        self._page = None

    async def __aenter__(self):
        """開啟異步上下文"""
        try:
            await self._start()
            return self
        except Exception as e:
            await self._stop()
            raise e

    async def __aexit__(self, exc_type, exc_value, traceback):
        """關閉異步上下文"""
        await self._stop()

    @abc.abstractmethod
    async def _start(self):
        """初始化引擎"""

    @abc.abstractmethod
    async def _stop(self):
        """關閉引擎"""

    def browser(self):
        """
        異步上下文呼叫介面
        async with obj.browser() as browser:
            ...
        """
        return self

    def page(self):
        """呼叫頁面"""
        return self._page