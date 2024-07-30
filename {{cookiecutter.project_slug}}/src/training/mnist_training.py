{% if cookiecutter.ml_framework == 'tensorflow' %}

import os
from data_loaders.mnist_data_loader import MNISTDataLoader
from models.simple_model_builder import SimpleModelBuilder
from training.training_interface import TrainingInterface


class MNISTTraining(TrainingInterface):
    def train(self):
        # Load data
        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load_data()

        # Build model
        simple_model_builder = SimpleModelBuilder()
        model = simple_model_builder.build_model()

        # Compile model
        model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )

        # Train model using training data
        model.fit(x_train, y_train, epochs=10, batch_size=32)

        # Save trained model to models folder
        model_dir = "../models"
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        model.save(os.path.join(model_dir, "mnist_model.h5"))

{% elif cookiecutter.ml_framework == 'pytorch' %}

import os
import torch
import torch.optim as optim
import torch.nn as nn
from data_loaders.mnist_data_loader import MNISTDataLoader
from models.simple_model_builder import SimpleModelBuilder
from training.training_interface import TrainingInterface

class MNISTTraining(TrainingInterface):
    def train(self):
        # Load data
        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load_data()

        # Build model
        model_builder = SimpleModelBuilder()
        model = model_builder.build_model()

        # Set up loss function and optimizer
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        # Training loop
        model.train()
        for epoch in range(10):  # number of epochs
            optimizer.zero_grad()
            outputs = model(x_train)
            loss = criterion(outputs, y_train)
            loss.backward()
            optimizer.step()
            print(f"Epoch {epoch+1}, Loss: {loss.item()}")

        # Save trained model
        model_dir = "../models"
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        torch.save(model.state_dict(), os.path.join(model_dir, "mnist_model.pth"))

{% endif %}
