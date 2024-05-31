# {{cookiecutter.project_name}}

## Table of Contents

- [Summary](#summary)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)

## Summary

{{ cookiecutter.description }}

**NOTE:** The content within the Python files in the [src folder](./src/) can be replaced. Initially model training and inference is showcased utilizing Keras with the MNIST dataset.

## Folder structure

```sh
project_root/
│
├── data/                   # Directory for storing datasets. NOTE: It is recommended to use an external BLOB storage for managing models to maintain a lean GitHub repository.
│   └── dataset/
│       └── ...
│
├── models/                 # Directory for storing trained models. NOTE: It is recommended to use an external BLOB storage for managing models to maintain a lean GitHub repository.
│   └── saved_models/
│       └── ...
│
├── src/                    # Source code directory
│   ├── data_loader.py      # Data loading utilities. Load the dataset from the specified directory (data/ in this case) or from external sources like databases or APIs
│   ├── model.py            # Model architecture definition
│   ├── train.py            # Training script saving trained model
│   ├── inference.py        # Inference script for testing the the saved model
│   └── utils.py            # Utility functions
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