import numpy as np

from src.tabular.core.base_job import BaseJob
import pandas as pd
from src.tabular.storage.csv_backend import CSVStorage


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
            self.data.dd[numericCols] = self.data.dd[numericCols].fillna(const)
        else :
            raise ValueError("Invalid method")

    def run(self,context : list[dict]):
        for task in context:
            function = getattr(self,str(task["function"]))
            params = task.get("params", {})
            function(**params)

