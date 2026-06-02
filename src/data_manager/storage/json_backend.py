from data_manager.storage.base import BaseStorage
import pandas as pd
class JSONStorage(BaseStorage):
    def __init__(self):
        super().__init__()
        self.dd=None
        self.path = None
    def load(self, path):
        self.path = path
        self.dd = pd.read_json(path)
    def write(self,path):
        path = path if path is not None else self.path
        self.dd.to_json(path, index=False)
    def store(self, data):
        self.dd = pd.DataFrame(data)