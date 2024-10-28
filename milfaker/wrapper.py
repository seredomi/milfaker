import faker
from milfaker.providers import MilitaryProvider


class MilitaryFaker(faker.Faker):
    def __init__(self, locale=None):
        super().__init__(locale)
        self.add_provider(MilitaryProvider)
