import pytest
from milfaker.wrapper import MilitaryFaker


@pytest.fixture
def mil_faker():
    mil_faker = MilitaryFaker()
    return mil_faker


@pytest.fixture
def num_samples():
    return 10


def test_sample(mil_faker, num_samples):
    for _ in range(num_samples):
        sample = mil_faker.sample()
        assert isinstance(sample, str)
