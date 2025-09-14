from playwright.async_api import async_playwright, Browser, Page
from .base import BaseEngine


class Playwright(BaseEngine[Browser, Page]):

    async def _start(self):
        """初始化引擎"""
        playwright_ = await async_playwright().start()
        self._browser = await playwright_.chromium.launch(headless=True)

    async def _stop(self):
        """關閉引擎"""
        await self._browser.close()
        self._browser = None

    async def new_page(self):
        return await self._browser.new_page()
