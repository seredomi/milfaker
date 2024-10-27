import pytest
import faker
from milfaker.providers import sample_provider


@pytest.fixture
def faker_fixture():
    fake = faker.Faker()
    fake.add_provider(sample_provider)
    return fake


@pytest.fixture
def num_samples():
    return 10


def test_sample(faker_fixture, num_samples):
    for _ in range(num_samples):
        sample = faker_fixture.sample()
        assert isinstance(sample, str)
        assert sample in sample_provider.elements
