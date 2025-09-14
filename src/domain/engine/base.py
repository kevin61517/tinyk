import abc


class EngineInterface:
    """爬蟲引擎介面"""
    @abc.abstractmethod
    async def __aenter__(self):
        """開啟異步上下文"""

    @abc.abstractmethod
    async def __aexit__(self, exc_type, exc_value, traceback):
        """關閉異步上下文"""
