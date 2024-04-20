from injector import Binder, Injector, Module, singleton

from src.pokeberry.domain.pokeberry_repository import PokeberryRepository
from src.pokeberry.infrastructure.pokeberry_repository import PokeberryApiRepository


class PokeberryDependencyContainer(Module):
    def __init__(self, injector: Injector) -> None:
        self.injector = injector

    def configure(self, binder: Binder) -> None:
        pokeberry_api_repository = PokeberryApiRepository()

        binder.bind(PokeberryRepository,
                    to=pokeberry_api_repository, scope=singleton)
