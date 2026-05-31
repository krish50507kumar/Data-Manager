from debugpy.launcher import output

from src.data_manager.core.base_job import BaseJob
import pandas as pd
class DataAnalytics(BaseJob):
    def __init__(self,data):
        super().__init__()
        self.data = data

    def duplicate_analysis(self):
        total_rows = self.data.dd.shape[0]
        duplicate_row =self.data.dd.duplicated().sum()
        output = {
            "No of duplicate rows":duplicate_row,
            "Duplicate row percentage":duplicate_row/total_rows*100
        }
        return output

    def missing_analysis(self):
        no_of_missing_rows = self.data.dd.isnull().any(axis=1).sum()
        total_rows = self.data.dd.shape[0]
        column_wise_null_count = self.data.dd.isnull().sum().to_dict()
        output = {
            "Total rows containing missing value":no_of_missing_rows,
            "Missing row percentage": no_of_missing_rows/total_rows*100,
            "Missing value per columns": column_wise_null_count
        }
        return output

    def run(self, context: list[dict]):
        for task in context:
            function = getattr(self, str(task["function"]))
            params = task.get("params", {})
            function(**params)
