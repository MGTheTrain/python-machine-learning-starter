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
