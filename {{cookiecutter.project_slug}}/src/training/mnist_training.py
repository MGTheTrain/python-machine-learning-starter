{% if cookiecutter.ml_framework == 'tensorflow' %}

from data_loaders.mnist_data_loader import MNISTDataLoader
from models.simple_nn import SimpleNN
from training.training_interface import TrainingInterface
import tensorflow as tf

class MNISTTraining(TrainingInterface):
    def train(self, model_path: str = "../models/mnist_model.h5", data_set_path: str = "") -> None:
        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load(data_set_path=data_set_path)

        # Split the training data into training and validation
        x_val, x_train = x_train[:5000], x_train[5000:]
        y_val, y_train = y_train[:5000], y_train[5000:]

        simple_nn = SimpleNN()
        model = simple_nn.build()

        model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )

        model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_val, y_val))

        model.save(model_path)

{% elif cookiecutter.ml_framework == 'pytorch' %}

import torch
import torch.optim as optim
import torch.nn as nn
from data_loaders.mnist_data_loader import MNISTDataLoader
from models.simple_nn import SimpleNN
from training.training_interface import TrainingInterface

class MNISTTraining(TrainingInterface):
    def train(self, model_path: str = "../models/mnist_model.h5", data_set_path: str = "") -> None:
        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load(data_set_path=data_set_path)

        # Split the training data into training and validation
        x_val, x_train = x_train[:5000], x_train[5000:]
        y_val, y_train = y_train[:5000], y_train[5000:]

        simple_nn = SimpleNN()
        model = simple_nn.build()

        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        model.train()
        for epoch in range(10):
            optimizer.zero_grad()
            outputs = model(x_train)
            loss = criterion(outputs, y_train)
            loss.backward()
            optimizer.step()
            print(f"Epoch {epoch+1}, Loss: {loss.item()}")

            # Validation after each epoch
            model.eval()  # Set the model to evaluation mode
            with torch.no_grad():  # Disable gradient computation for validation
                val_outputs = model(x_val)
                val_loss = criterion(val_outputs, y_val)
                val_accuracy = (val_outputs.argmax(dim=1) == y_val).float().mean()
                print(f"Validation Loss: {val_loss.item()}, Validation Accuracy: {val_accuracy.item()}")
            model.train()  # Set the model back to training mode

        torch.save(model.state_dict(), model_path)

{% endif %}
