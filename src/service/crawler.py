from typing import Optional
from src.domain.engine import EngineInterface
from src.infra.engine import engine_register


class Crawler:
    def __init__(self, engine_name: str, **options):
        self._engine_name: str = engine_name
        self._engine: Optional[EngineInterface] = None

    async def launch(self, **options):
        _Engine = engine_register.get(self._engine_name)
        self._engine = await _Engine.launch(**options)
        return self

    @property
    def engine(self):
        return self._engine
