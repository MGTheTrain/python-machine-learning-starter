# {{cookiecutter.project_name}}

## Table of Contents

- [Summary](#summary)
- [References](#references)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
- [Author](#author)

## Summary

{{ cookiecutter.description }}

**NOTE:** 

- The content within the Python files in the [src folder](./src/) can be replaced. Initially model training and inference is showcased utilizing {{ cookiecutter.ml_framework }} with the MNIST dataset.
{% if cookiecutter.ml_framework == 'pytorch' %}
- [Currently, PyTorch on Windows only supports Python 3.8-3.11; Python 2.x is not supported](https://pytorch.org/get-started/locally/)
{% endif %}

## References

- [dvc Github repository](https://github.com/iterative/dvc):

"Data Version Control or DVC is a command line tool and VS Code Extension to help you develop reproducible machine learning projects:

Version your data and models. Store them in your cloud storage but keep their version info in your Git repo.
Iterate fast with lightweight pipelines. When you make changes, only run the steps impacted by those changes.
Track experiments in your local Git repo (no servers needed).
Compare any data, code, parameters, model, or performance plots.
Share experiments and automatically reproduce anyone's experiment."

## Folder structure

```sh
project_root/
│
├── data/                   # Directory for storing datasets. NOTE: It is recommended to use an external BLOB storage for managing data to maintain a lean GitHub repository. Hence the dvc tool proves to be useful.
│   └── dataset/
│       └── ...
│
├── models/                 # Directory for storing trained models. 
│   └── saved_models/       # NOTE: It is recommended to use an external BLOB storage for managing models to maintain a lean GitHub repository. Hence the dvc tool proves to be useful.
│       └── ...
│
├── src/                    # Source code directory
│   ├── __init__.py
│   ├── data_loaders        # Data loading utilities. Load the dataset from the specified directory (data/ in this case) or from external sources like databases or APIs
│   │   ├── __init__.py
│   │   ├── data_loader_interface.py
│   │   └── mnist_data_loader.py
│   │   └── ...
│   ├── inferences          # Inference scripts for testing the saved model
│   │   ├── inference_interface.py
│   │   └── mnist_inference.py
│   │   └── ...
│   ├── models              # Model architecture definition
│   │   ├── __init__.py
│   │   ├── model_builder_interface.py
│   │   └── simple_model_builder.py
│   │   └── ...
│   ├── training            # Training scripts saving trained model
│   │   ├── __init__.py
│   │   ├── mnist_training.py
│   │   └── training_interface.py
│   │   └── ...
│   └── utils
│       ├── __init__.py
│       └── utils.py
│       └── ...
│   ├── main.py             # Entry point script for executing model training or inference
│   ├── ...                 # Other entrypoint scripts
│
├── tests/                  # Test directory
│   ├── test_model.py       
│   ├── data_loader.py      
│   ├── ...      
|
├── experiments/            # NOTE: Requires dvc tool. Directory for storing experiment configurations, results, and logs
│   ├── experiment_1/       # Store experiment-specific files and data here
│   │   ├── config.yaml     # Configuration file for experiment 1
│   │   ├── metrics.json    # Metrics recorded during experiment 1
│   │   └── logs/           # Logs generated during experiment 1
│   └── ...                 # Additional experiment directories
│
├── requirements.txt        # Python dependencies
├── README.md               # Project README file
├── Dockerfile              # Enables training in an isolated docker container
├── Makefile                # Entrypoint enabling useful commands
├── docs                    # Project documentation
├── scripts                 # Helper scripts
└── main.py                 # Entry point script for executing model training or inference
```

## Getting started

### Preconditions

- Preferably utilize the [devcontainer.json](./.devcontainer/devcontainer.json). Therefore use the [dev container feature in VS Code IDE](https://code.visualstudio.com/docs/devcontainers/containers) to setup the development container
- Install pip packages. Therefore run:

```sh
make setup
```

- Consider initial auto-formatting. Therefore run: 

```sh
make format-and-lint
```

### Training the model from the dataset

```sh
make train
```

### Model inference

```sh
make infer
```

### Run pytests

To run all tests:

```sh
make test
```

To run an individual test:

```sh
make test-individual filename=test_model.py
```

### Generating project documentation

```sh
make docs
```

### Auto-format and lint python files

```sh
make format-and-lint
```

**NOTE:** Optionally it is recommended to set up a symbolic link via `cd .git/hooks && ln -s ../../scripts/format_and_lint.sh pre-commit && sudo chmod +x pre-commit && cd -` and a validation automation workflow to ensure that the `format_and_lint.sh` script is executed with each commit.

### Clearing artifacts

```sh
make clean
```

## Author

{{ cookiecutter.author_name }}