# Variables
PYTHON = python3
PIP = pip3

# Directories
DOCS_DIR = docs
TEST_DIR = tests
SRC_DIR = src

# Commands
.PHONY: all setup test test-individual clean train inference docs format-and-lint

# Default target
all: setup docs

# Setup the environment
setup:
	$(PIP) install -r requirements.txt

# Run pytests (will also consider code coverage report generation)
test:
	pytest --cov --cov-report=xml --cov-report=term

test-individual:
	@if [ -z "$(filename)" ]; then \
		echo "Please provide a filename in the test folder using 'make test-individual filename=<e.g. test_model.py>'"; \
	else \
		pytest --cov --cov-report=xml --cov-report=term $(TEST_DIR)/$(filename); \
	fi

# Clean up generated files
clean:
	rm -rf $(DOCS_DIR)/_build
	find . -type d -name '*.pyc' -exec rm -rf {} +
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	rm -rf .coverage coverage.xml 
	rm -rf ${DOCS_DIR}/{{cookiecutter.project_slug}}/_site
	rm -rf ${DOCS_DIR}/{{cookiecutter.project_slug}}/.jekyll-cache
	echo "Manually clean contents in data and models dir"  

# Model training
train:
	cd $(SRC_DIR) && $(PYTHON) main.py --mode train

# Model inference
inference:
	cd $(SRC_DIR) && $(PYTHON) main.py --mode inference

# Build and serve documentation
docs:
	cd docs/{{cookiecutter.project_slug}} && jekyll serve && echo "Visit in a browser of choice localhost:4000"

format-and-lint:
	cd scripts && ./format_and_lint.sh