{% if cookiecutter.ml_framework == 'tensorflow' %}

from tensorflow.keras import layers, models
from src.models.simple_model_builder import SimpleModelBuilder


def test_build_model():
    simple_model_builder = SimpleModelBuilder()
    model = simple_model_builder.build_model()
    assert isinstance(model, models.Sequential)
    assert len(model.layers) == 3
    assert isinstance(model.layers[0], layers.Flatten)
    assert isinstance(model.layers[1], layers.Dense)
    assert isinstance(model.layers[2], layers.Dense)
    assert model.layers[1].units == 128
    assert model.layers[2].units == 10
    assert model.layers[2].activation.__name__ == "softmax"

{% elif cookiecutter.ml_framework == 'pytorch' %}

import torch
from src.models.simple_model_builder import SimpleModelBuilder

def test_build_model():
    simple_model_builder = SimpleModelBuilder()
    model = simple_model_builder.build_model()
    
    assert isinstance(model, torch.nn.Module)
    children = list(model.children())
    
    # Verify the number of layers
    assert len(children) == 5  # Flatten, Linear, ReLU, Linear, Softmax
    
    # Verify types of layers
    assert isinstance(children[0], torch.nn.Flatten)
    assert isinstance(children[1], torch.nn.Linear)
    assert isinstance(children[2], torch.nn.ReLU)
    assert isinstance(children[3], torch.nn.Linear)
    assert isinstance(children[4], torch.nn.Softmax)
    
    # Verify the properties of the linear layers
    assert children[1].out_features == 128
    assert children[3].out_features == 10

if __name__ == "__main__":
    test_build_model()
    print("All tests passed!")

{% endif %}
