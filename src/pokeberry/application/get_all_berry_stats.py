import json
from flask import Response
from flask_restful import Resource
from injector import inject

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

        berries_data = self.pokeberry_repository.get_berries(berries_ids)

        return Response(
            mimetype="application/json",
            response=json.dumps(berries_data),
            status=200,
        )
