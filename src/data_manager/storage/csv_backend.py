from data_manager.storage.base import BaseStorage
import pandas as pd
class CSVStorage(BaseStorage):
    def __init__(self):
        super().__init__()
        self.data = None
        self.path = None | str
    def store(self, data):
        self.data = data
    def load(self, path):
        self.path = path
        self.data = pd.read_csv(self.path)
    def write(self,path=None):
        path = path if path is not None else self.path
        self.data.to_csv(path, index=False)

