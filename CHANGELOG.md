# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.1] - 31-03-2025

### Fixed

- Added `install-gems` and updated `docs` targets in the Makefile. Also updated the required gems in `Gemfile` and `Gemfile.lock`

## [0.4.0] - 31-03-2025

### Updated

- Verified that the [architecture-doc folder structure]({{cookiecutter.project_slug}}/docs/{{cookiecutter.project_slug}}/pages/architecture-doc) follows the arc42 template

## [0.3.3] - 18-02-2025

### Fixed

- Considered validation during training

## [0.3.2] - 18-02-2025

### Fixed 

- Fixed signatures of abstract methods

## [0.3.1] - 18-02-2025

### Fixed 

- Refactored model build tests to use unittest.TestCase
- Fixed module imports

## [0.3.0] - 13-02-2025

### Updated

- Renamed files and methods in the Python `src` directory. Refactored method scopes to accept datasets and models as input arguments for training and inference
- Added a `help` target to the Makefile. Incorporated additional input arguments for the `train` and `infer` targets in the Makefile
- Added missing `__init__.py` file in `inferences` folder
- Overwritten CLI arguments with environment variables if they exist

### Removed

- Removed references in project template's `README.md`

## [0.2.1] - 07-02-2025

### Fixed

- Ensured correct `torch` pip package is installed

## [0.2.0] - 29-07-2024

### Updated

- Increase modularity by modifying project structure considering interfaces and classes
- Add a key-value in [cookiecutter.json](./cookiecutter.json) to select between Pytorch or Tensforflow setup 

## [0.1.0] - 01-06-2024

### Added

- Initial setup