from base import BaseStorage

class InMemoryStorage(BaseStorage):
    def __init__(self):
        super().__init__()
    def read(self, path):
        pass
    def write(self, path, data):
        self.dd = data
    def store(self, path, data):
        self.dd = data
        