from tabular.storage.base import BaseStorage
import pandas as pd
class CSVStorage(BaseStorage):
    def __init__(self):
        super().__init__()
        self.dd = None
    def store(self, data):
        self.dd = data
    def read(self, path):
        self.dd = pd.read_csv(path)
    def write(self, path , data):
        self.dd = data
        self.dd.to_csv(path)

