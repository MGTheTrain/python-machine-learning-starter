{% if cookiecutter.ml_framework == 'tensorflow' %}

from data_loaders.data_loader_interface import DataLoaderInterface
import tensorflow as tf

class MNISTDataLoader(DataLoaderInterface):
    def load_data(self):
        # Load MNIST dataset
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

        # Print shapes of loaded data
        print("x_train shape:", x_train.shape)
        print("y_train shape:", y_train.shape)
        print("x_test shape:", x_test.shape)
        print("y_test shape:", y_test.shape)

        # Normalize pixel values to the range [0, 1]
        x_train, x_test = x_train / 255.0, x_test / 255.0

        # Reshape images to have a channel dimension
        x_train = x_train[..., tf.newaxis]
        x_test = x_test[..., tf.newaxis]

        return (x_train, y_train), (x_test, y_test)

{% elif cookiecutter.ml_framework == 'pytorch' %}

from data_loaders.data_loader_interface import DataLoaderInterface
import torch
from torchvision import datasets, transforms

class MNISTDataLoader(DataLoaderInterface):
    def load_data(self):
        # Define a transform to normalize the data
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])

        # Load MNIST dataset
        train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
        test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

        train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
        test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)

        # Extract data and labels
        x_train, y_train = zip(*[batch for batch in train_loader])
        x_test, y_test = zip(*[batch for batch in test_loader])

        x_train = torch.cat(x_train)
        y_train = torch.cat(y_train)
        x_test = torch.cat(x_test)
        y_test = torch.cat(y_test)

        return (x_train, y_train), (x_test, y_test)
        
{% endif %}
