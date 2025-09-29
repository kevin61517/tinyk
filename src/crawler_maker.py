from src.infra.engine import engine_register
from src.service.crawler import Crawler


def crawler_maker(name: str) -> Crawler:
    _Engine = engine_register.get(name)
    return Crawler(_Engine)