"""
引擎管理：使用engine_factory初始化引擎。
"""
from typing import Type
from src.domain.engine import EngineInterface
from .base import BaseEngine
from .playwright import Playwright


Engine = BaseEngine


async def engine_factory(engine_manager: Type[EngineInterface], name: str, *args, **kws) -> EngineInterface:
    engine = engine_manager.use_engine(name.lower())
    return await engine(*args, **kws).init_engine()
