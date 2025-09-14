import asyncio
from src.infra.engine.playwright import Playwright


async def main():
    engine = Playwright()
    async with engine.browser() as browser:
        page = await browser.new_page()
        await page.goto('https://google.com')
        print(await page.title())


if __name__ == '__main__':
    asyncio.run(main())