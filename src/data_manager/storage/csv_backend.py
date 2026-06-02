from data_manager.storage.base import BaseStorage
import pandas as pd
class CSVStorage(BaseStorage):
    def __init__(self):
        super().__init__()
        self.dd = None
        self.path = None | str
    def store(self, data):
        self.dd = data
    def load(self, path):
        self.path = path
        self.dd = pd.read_csv(self.path)
    def write(self,path=None):
        path = path if path is not None else self.path
        self.dd.to_csv(path, index=False)

