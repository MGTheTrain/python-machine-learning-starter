from abc import ABC, abstractmethod

class DataLoaderInterface(ABC):
    @abstractmethod
    def load_data(self):
        pass