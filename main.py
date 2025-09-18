import asyncio

from src.infra.engine.playwright import Playwright
from src.infra.engine import engine_factory


async def main():
    engine = await engine_factory('Playwright')
    browser = await engine.init_browser('chromium')
    print('browser---->', browser)
    async with await browser.launch(headless=False) as b:
        page = await b.new_page()
        print(page)
        await page.goto('https://google.com')
        print(await page.title())


if __name__ == '__main__':
    asyncio.run(main())
    # print(dir(a))
