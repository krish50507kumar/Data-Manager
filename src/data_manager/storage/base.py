from abc import ABC, abstractmethod
class BaseStorage(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def read(self, path):
        pass
    @abstractmethod
    def write(self, data):
        pass
    @abstractmethod
    def store(self, data):
        pass
