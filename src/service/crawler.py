from typing import Type
from src.domain.engine import EngineInterface


class Crawler:
    def __init__(self, engine: Type[EngineInterface]):
        self._engine = engine

    async def launch(self, **options):
        self._engine = await self._engine.launch(**options)
        return self

    @property
    def engine(self):
        return self._engine
