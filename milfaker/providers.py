from faker.providers import DynamicProvider

sample_provider = DynamicProvider(
    provider_name="sample", elements=["sample1", "sample2", "sample3"]
)
