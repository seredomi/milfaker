help: ## this info
	@echo '_________________'
	@echo '| Make targets: |'
	@echo '-----------------'
	@echo
# The regex only grabs targets that include a "##" after their declaration.
	@cat Makefile | grep -E '^[0-9a-zA-Z\/_-]+:.*?## .*$$' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo

wheel: ## build wheel to package up this repo
	poetry build

test: format lint ## run tests
	poetry run coverage run -m pytest tests
	poetry run coverage report -m

lint: ## run linter
	poetry run ruff check

format: ## run formatter
	poetry run ruff format
