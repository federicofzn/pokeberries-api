from abc import ABC, abstractmethod
from typing import List

from src.pokeberry.domain.pokeberry import Pokeberry


class PokeberryRepository(ABC):
    """Abstract base class for pokeberries."""

    @abstractmethod
    def get_berries_count(self) -> int:
        """Get the count of berries from."""

    @abstractmethod
    def get_berry(self, berry_id) -> Pokeberry:
        """Get the berry by id."""

    @abstractmethod
    def get_berries(self, berries_id) -> List[Pokeberry]:
        """Get the berries by ids."""
