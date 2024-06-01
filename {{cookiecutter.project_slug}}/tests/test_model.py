import pytest
from tensorflow.keras import layers, models
from src.model import build_model

def test_build_model():
    model = build_model()
    assert isinstance(model, models.Sequential)
    assert len(model.layers) == 3
    assert isinstance(model.layers[0], layers.Flatten)
    assert isinstance(model.layers[1], layers.Dense)
    assert isinstance(model.layers[2], layers.Dense)
    assert model.layers[1].units == 128
    assert model.layers[2].units == 10
    assert model.layers[2].activation.__name__ == "softmax"