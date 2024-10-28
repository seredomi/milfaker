import pytest
from milfaker.wrapper import MilitaryFaker


@pytest.fixture
def mil_faker():
    mil_faker = MilitaryFaker()
    return mil_faker


@pytest.fixture
def num_samples():
    return 10


def test_branch(mil_faker, num_samples):
    for _ in range(num_samples):
        simple_branch = mil_faker.military_branch(simple=True)
        assert isinstance(simple_branch, str)
        assert len(simple_branch.split(" ")) <= 2

    for _ in range(num_samples):
        complex_branch = mil_faker.military_branch(simple=False)
        assert isinstance(complex_branch, str)
        assert len(complex_branch.split(" ")) >= 2
