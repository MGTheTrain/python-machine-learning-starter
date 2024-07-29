from tensorflow.keras import layers, models
from models.model_builder_interface import ModelBuilderInterface

class SimpleModelBuilder(ModelBuilderInterface):
    def build_model(self):
        model = models.Sequential(
            [
                layers.Flatten(input_shape=(28, 28)),
                layers.Dense(128, activation="relu"),
                layers.Dense(10, activation="softmax"),
            ]
        )
        model.summary()
        return model