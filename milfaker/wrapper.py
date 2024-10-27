import faker
import milfaker.providers as p


class MilitaryFaker(faker.Faker):
    def __init__(self, locale=None):
        super().__init__(locale)
        self.add_provider(p.sample_provider)
