import os

from typing import List

import requests

from src.pokeberry.domain.pokeberry import Pokeberry
from src.pokeberry.domain.pokeberry_repository import PokeberryRepository


class PokeberryApiRepository(PokeberryRepository):
    """Repository class that interacts with pokeapi."""
    base_url = os.getenv("POKEAPI_URL")

    def fetch_data(self, url) -> requests.Response:
        """Fetch data from pokeapi."""
        return requests.get(url, timeout=2000)

    def get_berries_count(self) -> int:
        """Get the count of berries from pokeapi."""
        berries_url = self.base_url + "/berry"
        response = self.fetch_data(berries_url)
        count = response.json()["count"]

        return count

    def get_berry(self, berry_id) -> Pokeberry:
        """Get the berry by id from pokeapi."""

    def get_berries(self, berries_id) -> List[Pokeberry]:
        """Get the berries by ids from pokeapi."""
