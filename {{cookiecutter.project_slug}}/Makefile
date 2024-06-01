# Variables
PYTHON = python3
PIP = pip3

# Directories
DOCS_DIR = docs
SRC_DIR = src

# Commands
.PHONY: all setup clean train inference docs format

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
	rm -rf ${DOCS_DIR}/{{cookiecutter.project_slug}}/_site
	rm -rf ${DOCS_DIR}/{{cookiecutter.project_slug}}/.jekyll-cache
	echo "Manually clean contents in data and models dir"  

# Model training
train:
	$(PYTHON) main.py --mode train

# Model inference
inference:
	$(PYTHON) main.py --mode inference

# Build and serve documentation
docs:
	cd docs/{{cookiecutter.project_slug}} && jekyll serve && echo "Visit in a browser of choice localhost:4000"

format:
	cd scripts && ./format_and_lint.sh