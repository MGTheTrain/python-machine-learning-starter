from abc import ABC, abstractmethod

class InferenceInterface(ABC):
    @abstractmethod
    def train(self):
        pass
