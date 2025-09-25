"""
引擎管理：使用engine_factory初始化引擎。
"""
from .base import EngineRegister
from .playwright import Playwright


engine_register = EngineRegister()
engine_register.register(Playwright)
