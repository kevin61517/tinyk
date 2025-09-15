import asyncio
from src.infra.engine.playwright import Playwright


async def main():
    engine = Playwright()
    async with engine.browser() as browser:  # 上下文開啟  __aenter__
        page = await browser.new_page()
        await page.goto('https://google.com')
        print(await page.title())
    # 上下文關閉  __aexit__


if __name__ == '__main__':
    asyncio.run(main())