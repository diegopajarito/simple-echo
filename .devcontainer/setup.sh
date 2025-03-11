#!/usr/bin/env bash

git config --global --add safe.directory '*'

# # Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
uv sync

exit 0