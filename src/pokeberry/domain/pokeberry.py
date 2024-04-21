class Pokeberry():
    """Object class with the needed fields for a pokeberry."""

    def __init__(self, id: int, name: str, growth_time: int) -> None:
        self.id = id
        self.name = name
        self.growth_time = growth_time
