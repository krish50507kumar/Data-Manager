from base import BaseStorage

class InMemoryStorage(BaseStorage):
    def __init__(self):
        super().__init__()
        self.path = None | str
        self.dd = None
    def load(self, path):
        self.path = path
        pass
    def write(self, path, data):
        self.dd = data
    def store(self, data):
        self.dd = data
        