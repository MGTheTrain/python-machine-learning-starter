from abc import ABC, abstractmethod


class ModelBuilderInterface(ABC):
    @abstractmethod
    def build_model(self):
        pass
