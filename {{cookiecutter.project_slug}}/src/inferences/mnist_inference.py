import os
import numpy as np
from tensorflow.keras.models import load_model
from data_loaders.mnist_data_loader import MNISTDataLoader
from inferences.inference_interface import InferenceInterface


class MNISTInference(InferenceInterface):
    def infer(self):
        # Load saved model
        model_path = os.path.join("../models", "mnist_model.h5")
        model = load_model(model_path)

        # Load data for inference
        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load_data()

        # Perform inference
        predictions = model.predict(x_test)
        predicted_labels = np.argmax(predictions, axis=1)

        # Output predictions or perform further processing
        print("Predicted labels:", predicted_labels)
