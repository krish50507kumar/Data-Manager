from datetime import datetime

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

    def column_stats(self,column = None):
        if column is None:
            column = self.data.dd.iloc[0]
        output = self.data.dd.column.describe().to_dict()
        return output

    def summary(self):
        output = {
            "Rows":self.data.dd.shape[0],
            "Columns":self.data.dd.shape[1],
            "Data type":self.data.dd.dtypes,
            "Memory usage(Bytes)":self.data.dd.memory_usage(deep=True).sum(),
            "Missing values":self.data.dd.isnull().sum().to_dict()
        }
        return output

    def groupby_analysis(self,group_col,agg_col,agg_func,dropna = True):
        output = self.data.dd.groupby(group_col,dropna)[agg_col].agg(agg_func).to_dict()
        return output

    def profile(self):
        missing_report = self.missing_analysis()
        duplicate_report = self.duplicate_analysis()
        output = {
            "generated_at": datetime.now().isoformat(),
            "dataset_info": self.summary(),
            "missing_values": missing_report,
            "duplicate_values": duplicate_report,
            "numeric_columns": self.data.dd.select_dtypes(include=['number']).describe().to_dict(),
            "categorical_columns": self.data.dd.select_dtypes( include=['object', 'category']).describe().to_dict(),
            "quality_report":{
                "missing_percentage":missing_report["Missing row percentage"],
                "duplicate_percentage":duplicate_report["Duplicate row percentage"],
            }
        }

        return output

    def run(self, context: list[dict]):
        for task in context:
            function = getattr(self, str(task["function"]))
            params = task.get("params", {})
            function(**params)
