# Description: Makefile for managing the project
## Instuctions:
# run `make help` to see all available commands

# To add a new command, copy the following:
# Warning: The space between start of the line and @ SHOULD be tab space
# Tip: Uncomment the following lines to see the command in the help message

# .PHONY: command_name
# command_name: ## Description of the command
# 	@echo "Running command_name"

.PHONY: help
help: ## Show this help message
	@uv run python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
