from __future__ import annotations
import abc
from typing import Dict, Generic, TypeVar, Type
from collections.abc import Iterable


class RegistrableInterface(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def get_name(cls) -> str:
        """被註冊的名稱"""


T = TypeVar('T', bound=RegistrableInterface)


class RegisterInterface(abc.ABC, Generic[T]):
    """註冊介面"""

    def __init__(self):
        self._registry: Dict[str, Type[T]] = {}

    @abc.abstractmethod
    def get(self, name: str) -> Type[T]:
        """取得被註冊的物件"""

    @abc.abstractmethod
    def register(self, cls: Type[T]):
        """註冊"""

    @property
    @abc.abstractmethod
    def registries(self) -> Iterable[T]:
        """枚舉註冊物件"""