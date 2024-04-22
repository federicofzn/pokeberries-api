from collections import defaultdict
from typing import Dict, List

from src.pokeberry.domain.pokeberry import Pokeberry


class PokeberriesStatistics():
    """Class to perform statistics calculations for a pokeberry list."""

    def __init__(self, pokeberries: List[Pokeberry]) -> None:
        self.pokeberries = pokeberries
        self.pokeberries_len = len(pokeberries)
        self.growth_times = [
            pokeberry.growth_time for pokeberry in pokeberries]

    def get_min(self) -> int:
        """Returns the min growth_time from the list."""
        return min(self.growth_times)

    def get_median(self) -> int:
        """
          Returns the median growth_time from the list. 
          If the list is even, the median is the average of the two middle values.
        """
        sorted_growth_times = sorted(self.growth_times)

        n = self.pokeberries_len

        if n % 2 == 0:
            return (sorted_growth_times[n // 2 - 1] + sorted_growth_times[n // 2]) / 2

        return sorted_growth_times[n // 2]

    def get_max(self) -> int:
        """Returns the max growth_time from the list."""
        return max(self.growth_times)

    def get_variance(self) -> float:
        """
          Returns the variance growth_time from the list.
          Variance measures the average squared deviation of each number from its mean.
        """
        mean = self.get_mean()
        sum_squared_diff = sum((growth_time - mean) **
                               2 for growth_time in self.growth_times)
        return sum_squared_diff / self.pokeberries_len

    def get_mean(self) -> float:
        """Returns the mean growth_time from the list."""
        return sum(self.growth_times) / self.pokeberries_len

    def get_frequency(self) -> Dict:
        """Returns a dict with growth_time as key and berry names as value."""
        frequencies_dict = defaultdict(list)

        for pokeberry in self.pokeberries:
            frequencies_dict[pokeberry.growth_time].append(
                pokeberry.name)

        return dict(frequencies_dict)
