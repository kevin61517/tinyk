import asyncio

from src.infra.engine import engine_factory, Engine


async def main():
    # 設置測試參數
    engine_name = 'Playwright'  # 引擎
    browser_name = 'Chromium'  # 瀏覽器
    url = 'https://google.com'  # 頁面
    headless = False

    # 初始化測試物件
    engine = await engine_factory(Engine, engine_name)
    browser = await engine.init_browser(browser_name)

    # 開始測試
    async with await browser.launch(headless=headless) as b:
        page = await b.new_page()
        await page.goto(url)
        print(await page.title())
        await asyncio.sleep(3)


if __name__ == '__main__':
    asyncio.run(main())
