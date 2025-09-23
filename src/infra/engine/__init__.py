"""
引擎管理：使用engine_factory初始化引擎。
"""
from src.domain.engine import EngineInterface
from .base import EngineRegister, RegisterInterface
from .playwright import Playwright


engine_register = EngineRegister()
engine_register.register(Playwright)
