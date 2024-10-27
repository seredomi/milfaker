# milfaker
this is a simple library for generating fake military data

in an ideal world, this library could mature and be merged into the [Faker package](https://pypi.org/project/Faker/)

for now, the goal is to
- define military specific providers which can be imported and added to an existing faker instance
- provide a faker wrapper which implements these providers

## install
1. from this root dir, run `poetry build`
2. from your project, run `pip install path/to/milfaker/dist/milfaker-0.1.0-py3-none-any.whl`

(can publish to PyPi once it's ready)


## usage
### use specific providers
```python
import faker
from milfaker.providers import PaygradeProvider

my_faker = Faker()
my_faker.add_provider(PaygradeProvider)

paygrade = my_faker.paygrade(echelon='officer')
```

### use the wrapper
```python
from milfaker.wrapper import MilitaryFaker

my_faker = MilitaryFaker()
paygrade = my_faker.paygrade(echelon='officer')
```
