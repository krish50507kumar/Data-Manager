from data_manager.storage.base import BaseStorage
import pandas as pd
class JSONStorage(BaseStorage):
    def __init__(self):
        super().__init__()
        self.data=None
        self.path = None
    def load(self, path):
        self.path = path
        self.data = pd.read_json(path)
    def write(self,path):
        path = path if path is not None else self.path
        self.data.to_json(path, index=False)
    def store(self, data):
        self.data = pd.DataFrame(data)