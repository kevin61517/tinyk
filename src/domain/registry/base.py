from __future__ import annotations
import abc
from typing import Dict, Generic, TypeVar, Type, Generator
from collections.abc import Iterable


class RegistrableInterface(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def get_name(cls) -> str:
        """被註冊的名稱"""


T = TypeVar('T')


class RegisterInterface(abc.ABC, Generic[T]):
    """註冊介面"""

    def __init__(self):
        self._registry: Dict[str, T] = {}

    @abc.abstractmethod
    def get(self, name: str) -> T:
        """取得被註冊的物件"""

    @abc.abstractmethod
    def register(self, cls, **kws):
        """註冊"""

    @property
    @abc.abstractmethod
    def registries(self) -> Generator[str, T]:
        """枚舉註冊物件"""