from typing import Callable, Coroutine, Optional
from playwright.async_api import (
    async_playwright,
    Browser as PBrowser,
    Page as PPage,
    BrowserType,
    PlaywrightContextManager,
    Playwright as AsyncPlaywright
)
from .base import BaseEngine, BaseBrowser, BrowserInterface, BasePage


class Playwright(BaseEngine[PlaywrightContextManager]):

    async def _init(self, *args, **kws):
        return async_playwright()

    async def _init_browser(self, name: str) -> BrowserInterface:
        return Browser(browser=None, name=name, launcher=self._engine)

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__


class Browser(BaseBrowser[PBrowser]):
    """瀏覽器實作"""

    def __init__(self, browser, name: str, launcher: PlaywrightContextManager, *args, **kws):
        self._launcher = launcher
        self._name = name
        self._engine: Optional[AsyncPlaywright] = None
        super().__init__(browser, *args, **kws)

    async def _init_browser(self, *args, **kws):
        """初始化瀏覽器"""
        self._engine: AsyncPlaywright = await self._launcher.start()
        if not hasattr(self._engine, self._name):
            raise TypeError(f'Engine "{self.__class__.__name__}" has no browser "{self._name}"')

        browser: BrowserType = getattr(self._engine, self._name)
        if not isinstance(browser, BrowserType):
            raise TypeError(f'{self._name} is not a browser.')

        self._browser: PBrowser = await browser.launch(*args, **kws)

    async def _shutdown_browser(self):
        try:
            await self._browser.close()
            await self._engine.stop()
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

