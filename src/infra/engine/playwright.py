from playwright.async_api import (
    Browser as PBrowser,
    Page as PPage,
    BrowserType,
    async_playwright
)
from playwright.async_api._generated import Playwright as AsyncPlaywright
from .base import BaseEngine, BaseBrowser, BasePage


_NAME = 'Playwright'


class Playwright(BaseEngine[BrowserType]):

    def __init__(self, engine: AsyncPlaywright):
        """初始化"""
        self._engine: AsyncPlaywright = engine

    @classmethod
    def get_name(cls) -> str:
        return _NAME

    @classmethod
    async def launch(cls, **options):
        return cls(engine=await async_playwright().start())

    async def shutdown(self, **kws) -> None:
        await self._engine.stop()

    def get_browser(self, name: str):
        if isinstance(browser := getattr(self._engine, name), BrowserType):
            return browser
        raise TypeError(f'{name} is not a Browser.')


class Browser(BaseBrowser[BrowserType, PBrowser]):
    """瀏覽器實作"""

    @classmethod
    def get_name(cls) -> str:
        return _NAME

    async def _launch(self):
        """啟動瀏覽器"""
        self._browser = await self._launcher.launch(**self._options)

    async def _shutdown(self):
        try:
            await self._browser.close()
        except Exception as e:
            raise e

    async def new_page(self, *args, **kws):
        return await self._browser.new_page(*args, **kws)


class Page(BasePage[PPage]):
    """PlayWright Page 實作"""
    async def goto(self, url, *args, **kws):
        return await self._page.goto(url, *args, **kws)

    async def title(self, *args, **kws) -> str:
        return await self._page.title()

