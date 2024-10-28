import pytest
import faker
from milfaker.providers import MilitaryProvider


@pytest.fixture
def faker_fixture():
    fake = faker.Faker()
    fake.add_provider(MilitaryProvider)
    return fake


@pytest.fixture
def num_samples():
    return 10


def test_branch(faker_fixture, num_samples):
    for _ in range(num_samples):
        simple_branch = faker_fixture.military_branch(simple=True)
        assert isinstance(simple_branch, str)
        assert len(simple_branch.split(" ")) <= 2

    for _ in range(num_samples):
        complex_branch = faker_fixture.military_branch(simple=False)
        assert isinstance(complex_branch, str)
        assert len(complex_branch.split(" ")) >= 2
