{% if cookiecutter.ml_framework == 'tensorflow' %}

import unittest
from tensorflow.keras import layers, models
from models.simple_nn import SimpleNN

class TestBuildModel(unittest.TestCase):
    def test_build(self):        
        simple_nn = SimpleNN()
        model = simple_nn.build()

        self.assertIsInstance(model, models.Sequential)
        
        self.assertEqual(len(model.layers), 3)
        
        self.assertIsInstance(model.layers[0], layers.Flatten)
        self.assertIsInstance(model.layers[1], layers.Dense)
        self.assertIsInstance(model.layers[2], layers.Dense)
        
        self.assertEqual(model.layers[1].units, 128)
        self.assertEqual(model.layers[2].units, 10)
        
        self.assertEqual(model.layers[2].activation.__name__, "softmax")

if __name__ == "__main__":
    unittest.main()

{% elif cookiecutter.ml_framework == 'pytorch' %}

import unittest
import torch
from models.simple_nn import SimpleNN

class TestBuildModel(unittest.TestCase):
    def test_build(self):
        simple_nn = SimpleNN()
        model = simple_nn.build()
        
        self.assertIsInstance(model, torch.nn.Module)

        children = list(model.children())
        self.assertEqual(len(children), 5)  
        
        self.assertIsInstance(children[0], torch.nn.Flatten)
        self.assertIsInstance(children[1], torch.nn.Linear)
        self.assertIsInstance(children[2], torch.nn.ReLU)
        self.assertIsInstance(children[3], torch.nn.Linear)
        self.assertIsInstance(children[4], torch.nn.Softmax)
        
        self.assertEqual(children[1].out_features, 128)
        self.assertEqual(children[3].out_features, 10)

if __name__ == "__main__":
    unittest.main()

{% endif %}
