"""
引擎實作
 - playwright
 - Selenium
 - pyppeteer
"""
from .base import BaseEngine


def engine_factory(name: str, *args, **kws):
    engine = BaseEngine.use_engine(name.lower())
    return engine(*args, **kws).init_engine()
