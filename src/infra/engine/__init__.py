"""
引擎管理：使用engine_factory初始化引擎。
"""
from src.domain.engine import EngineInterface
from .base import EngineRegister
from .playwright import Playwright


engine_register = EngineRegister()
engine_register.register(Playwright)


async def engine_factory(name: str, *args, **kws) -> EngineInterface:
    engine = engine_register.get(name.lower())
    return await engine(*args, **kws).init_engine()
