from abc import ABC, abstractmethod
class BaseStorage(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def load(self, path):
        pass
    @abstractmethod
    def write(self, path):
        pass
    @abstractmethod
    def store(self, data):
        pass
