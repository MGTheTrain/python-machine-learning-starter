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
    assert len(list(model.children())) == 3  # Assuming you have a Flatten layer
    
    assert isinstance(model[0], torch.nn.Flatten)
    assert isinstance(model[1], torch.nn.Linear)
    assert isinstance(model[2], torch.nn.Linear)
    assert model[1].out_features == 128
    assert model[2].out_features == 10
    assert isinstance(model[2].activation, torch.nn.Softmax)  # Adjust according to actual implementation

{% endif %}
