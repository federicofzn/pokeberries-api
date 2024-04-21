import json


class Pokeberry():
    """Object class with the needed fields for a pokeberry."""

    def __init__(self, id, growth_time, name) -> None:
        self.id = id
        self.growth_time = growth_time
        self.name = name

    def to_json(self):
        """Returns a json representation of the object."""
        return json.dumps(self.__dict__)
