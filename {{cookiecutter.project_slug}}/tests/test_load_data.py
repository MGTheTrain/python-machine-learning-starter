{% if cookiecutter.ml_framework == 'tensorflow' %}

import unittest
from src.data_loaders.mnist_data_loader import MNISTDataLoader


class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load_data()

        # Check data shapes
        self.assertEqual(x_train.shape, (60000, 28, 28, 1))
        self.assertEqual(y_train.shape, (60000,))
        self.assertEqual(x_test.shape, (10000, 28, 28, 1))
        self.assertEqual(y_test.shape, (10000,))

        # Check data normalization
        self.assertTrue((x_train >= 0).all() and (x_train <= 1).all())
        self.assertTrue((x_test >= 0).all() and (x_test <= 1).all())

{% elif cookiecutter.ml_framework == 'pytorch' %}

import unittest
import torch
from src.data_loaders.mnist_data_loader import MNISTDataLoader

class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load_data()

        # Check data shapes
        self.assertEqual(x_train.shape, torch.Size([60000, 1, 28, 28]))
        self.assertEqual(y_train.shape, torch.Size([60000]))
        self.assertEqual(x_test.shape, torch.Size([10000, 1, 28, 28]))
        self.assertEqual(y_test.shape, torch.Size([10000]))

        # Check data normalization
        self.assertTrue(torch.all(x_train >= -1) and torch.all(x_train <= 1))
        self.assertTrue(torch.all(x_test >= -1) and torch.all(x_test <= 1))

{% endif %}

if __name__ == "__main__":
    unittest.main()