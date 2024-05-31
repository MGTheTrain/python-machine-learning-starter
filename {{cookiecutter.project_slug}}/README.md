# {{cookiecutter.project_name}}

## Table of Contents

- [Summary](#summary)
- [References](#references)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)

## Summary

{{ cookiecutter.description }}

**NOTE:** The content within the Python files in the [src folder](./src/) can be replaced. Initially model training and inference is showcased utilizing Keras with the MNIST dataset.

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
├── data/                   # Directory for storing datasets. NOTE: It is recommended to use an external BLOB storage for managing data to maintain a lean GitHub repository.
│   └── dataset/
│       └── ...
│
├── models/                 # Directory for storing trained models. 
│   └── saved_models/       # NOTE: It is recommended to use an external BLOB storage for managing models to maintain a lean GitHub repository.
│       └── ...
│
├── src/                    # Source code directory
│   ├── data_loader.py      # Data loading utilities. Load the dataset from the specified directory (data/ in this case) or from external sources like databases or APIs
│   ├── model.py            # Model architecture definition
│   ├── train.py            # Training script saving trained model
│   ├── inference.py        # Inference script for testing the saved model
│   └── utils.py            # Utility functions
│
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
└── main.py                 # Main entry point script for running the application
```

## Getting started

### Training the model from the dataset

Run:

```sh
 python main.py --mode train
 ```

 ### Model inference

Run:

 ```sh
 python main.py --mode inference
 ```