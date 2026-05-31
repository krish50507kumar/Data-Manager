from data_manager.storage.base import BaseStorage
import pandas as pd
class JSONStorage(BaseStorage):
    def __init__(self):
        super().__init__()
        self.dd=None
        self.path = None | str
    def read(self, path):
        self.path = path
        self.dd = pd.read_json(path)
    def write(self,data):
        self.dd.to_json(self.path, index=False)
    def store(self, data):
        self.dd = pd.DataFrame(data)