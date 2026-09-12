from abc import ABC, abstractmethod
from typing import Self


class Configurable[Configuration](ABC):
    @classmethod
    @abstractmethod
    def from_configuration(cls, configuration: Configuration) -> Self: ...
