# Variables
PYTHON = python3
PIP = pip3

# Directories
DOCS_DIR = docs
SRC_DIR = src
TEST_DIR = tests

# Commands
.PHONY: all setup clean docs tests

# Default target
all: setup docs tests

# Setup the environment
setup:
	$(PIP) install -r requirements.txt

# Clean up generated files
clean:
	rm -rf $(DOCS_DIR)/_build
	rm -rf $(SRC_DIR)/*.pyc
	rm -rf $(SRC_DIR)/__pycache__
	rm -rf $(TEST_DIR)/*.pyc
	rm -rf $(TEST_DIR)/__pycache__

# Build the documentation
docs:
	$(MAKE) -C $(DOCS_DIR) html

# Run tests
tests:
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

# Run a specific test file
test-%:
	$(PYTHON) -m unittest $(TEST_DIR)/$*.py
