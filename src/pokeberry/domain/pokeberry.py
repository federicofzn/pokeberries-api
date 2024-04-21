class Pokeberry():
    """Object class with the needed fields for a pokeberry."""

    def __init__(self, id: int, growth_time: int, name: str) -> None:
        self.id = id
        self.growth_time = growth_time
        self.name = name
