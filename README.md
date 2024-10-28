# milfaker
this is a simple library for generating fake military data

in an ideal world, this library could mature and be merged into the [Faker package](https://pypi.org/project/Faker/)

for now, the goal is to
- define a military specific provider which can be imported and added to an existing faker instance
- provide a ready-to-go faker wrapper which implements this provider

## install
1. from this root dir, run `poetry build`
2. from your project, run `pip install path/to/milfaker/dist/milfaker-0.1.0-py3-none-any.whl`

(can be published to PyPi when it's ready)


## usage
### use the provider
```python
import faker
from milfaker.providers import MilitaryProvider

my_faker = Faker()
my_faker.add_provider(MilitaryProvider)

paygrade = my_faker.rank(branch='Army', rank_tier='Enlisted')
```

### use the wrapper
```python
from milfaker.wrapper import MilitaryFaker

my_faker = MilitaryFaker()
paygrade = my_faker.rank(branch='Army', echelon='Enlisted')
```
