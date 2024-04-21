from unittest import mock
from faker import Faker
from src.pokeberry.application.get_all_berry_stats import GetAllBerryStats
from src.pokeberry.domain.pokeberry import Pokeberry


def test_get_all_berry_stats():
    """Test for get all berry stats use case"""
    fake = Faker()

    pokeberries = [
        Pokeberry(fake.uuid4(), fake.name(), 2),
        Pokeberry(fake.uuid4(), fake.name(), 4),
        Pokeberry(fake.uuid4(), fake.name(), 6),
        Pokeberry(fake.uuid4(), fake.name(), 2),
        Pokeberry(fake.uuid4(), fake.name(), 8),
    ]

    pokeberry_repository = mock.MagicMock()
    pokeberry_repository.get_berries.return_value = pokeberries

    response = GetAllBerryStats(pokeberry_repository).get()
    response = response.json

    expected = {
        "berries_names": [berry.name for berry in pokeberries],
        "min_growth_time": 2,
        "median_growth_time": 4,
        "max_growth_time": 8,
        "variance_growth_time": 5.4399999999999995,
        "mean_growth_time": 4.4,
        "frequency_growth_time": 0,
    }

    assert all(
        pokeberry.name in response.get("berries_names") for pokeberry in pokeberries)
    assert response.get(
        "min_growth_time") == expected["min_growth_time"]
    assert response.get(
        "median_growth_time") == expected["median_growth_time"]
    assert response.get(
        "max_growth_time") == expected["max_growth_time"]
    assert response.get(
        "variance_growth_time") == expected["variance_growth_time"]
    assert response.get(
        "mean_growth_time") == expected["mean_growth_time"]
    assert response.get(
        "frequency_growth_time") == expected["frequency_growth_time"]
