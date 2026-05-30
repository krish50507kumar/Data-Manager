import numpy as np

from src.data_manager.core.base_job import BaseJob
import pandas as pd
from src.data_manager.storage.csv_backend import CSVStorage


class DataEngineer(BaseJob):
    def __init__(self,data : CSVStorage):
        super().__init__()
        self.data = data

    def removeDublicate(self):
        self.data.dd.drop_duplicates()

    def removeNull(self,method = "drop",const = 0):
        if method == "drop":
            self.data.dd.dropna(inplace=True)
        elif method == "const":
            numericCols = self.data.dd.select_dtypes(include=np.number).columns
            objectCols = self.data.dd.select_dtypes(exclude=np.number).columns
            self.data.dd[numericCols] = self.data.dd[numericCols].fillna(const)
            self.data.dd[objectCols] = self.data.dd[objectCols].fillna("Unknown")
        else :
            raise ValueError("Invalid method")

    def run(self,context : list[dict]):
        for task in context:
            function = getattr(self,str(task["function"]))
            params = task.get("params", {})
            function(**params)

