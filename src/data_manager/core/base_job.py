from abc import ABC, abstractmethod

class BaseJob(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def run(self,context):
        pass

    def savepoint(self,name):
        self.storage.savepoint(name)
    def roleback(self):
        self.storage.roleback()