from abc import ABC, abstractmethod

class BaseJob(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def run(self,context):
        pass

