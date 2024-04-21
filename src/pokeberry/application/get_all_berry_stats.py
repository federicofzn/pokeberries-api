import json
from flask import Response
from flask_restful import Resource
from injector import inject

from src.pokeberry.domain.pokeberries_statistics import PokeberriesStatistics
from src.pokeberry.domain.pokeberry_repository import PokeberryRepository


class GetAllBerryStats(Resource):
    """RESTful resource that expose methods for allBerryStats endpoint"""
    @inject
    def __init__(self, pokeberry_repository: PokeberryRepository) -> None:
        self.pokeberry_repository = pokeberry_repository

    def get(self):
        """GET method."""
        berries_count = self.pokeberry_repository.get_berries_count()

        berries_ids = range(1, berries_count)

        pokeberries = self.pokeberry_repository.get_berries(berries_ids)

        pokeberries_stats = PokeberriesStatistics(pokeberries)

        response = {
            "berries_names": [berry.name for berry in pokeberries],
            "min_growth_time": pokeberries_stats.get_min(),
            "median_growth_time": pokeberries_stats.get_median(),
            "max_growth_time": pokeberries_stats.get_max(),
            "variance_growth_time": pokeberries_stats.get_variance(),
            "mean_growth_time": pokeberries_stats.get_mean(),
            "frequency_growth_time": pokeberries_stats.get_frequency()
        }

        return Response(
            mimetype="application/json",
            response=json.dumps(response),
            status=200,
        )
