# Variables
PYTHON = python3
PIP = pip3

# Directories
DOCS_DIR = docs
SRC_DIR = src

# Commands
.PHONY: all setup clean docs

# Default target
all: setup docs

# Setup the environment
setup:
	$(PIP) install -r requirements.txt

# Clean up generated files
clean:
	rm -rf $(DOCS_DIR)/_build
	rm -rf $(SRC_DIR)/*.pyc
	rm -rf $(SRC_DIR)/__pycache__

# Build and serve documentation
docs:
	cd docs && jekyll serve && echo "Visit in a browser of choice localhost:4000"