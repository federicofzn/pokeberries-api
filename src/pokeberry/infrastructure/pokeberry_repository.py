import os

from concurrent.futures import ThreadPoolExecutor
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
        berry_url = self.base_url + f"/berry/{berry_id}"
        response = self.fetch_data(berry_url)
        berry_data = response.json()

        return berry_data

    def get_berries(self, berries_id) -> List[Pokeberry]:
        """Get the berries by ids from pokeapi."""
        berries_data = []

        with ThreadPoolExecutor() as executor:
            # Submit the get_berry requests
            berries_requests = [executor.submit(self.get_berry, id)
                                for id in berries_id]

            # Gather the get_berry results
            for berry_request in berries_requests:
                result = berry_request.result()

                if result:
                    berries_data.append(result)

        return berries_data
