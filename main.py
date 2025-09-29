import asyncio
from src.crawler_maker import crawler_maker


async def main():
    # 設置測試參數
    engine_name = 'Playwright'  # 引擎
    browser_name = 'Chromium'  # 瀏覽器
    url = 'https://google.com'  # 頁面
    headless = False

    # 初始化測試物件
    crawler = crawler_maker(engine_name)
    await crawler.launch()  # 啟動引擎
    print(crawler.engine)
    await crawler.engine.shutdown()  # 關閉引擎


if __name__ == '__main__':
    asyncio.run(main())
