from datetime import datetime
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("DataManager")

from data_manager.core.base_job import BaseJob
import pandas as pd
class DataAnalytics(BaseJob):
    def __init__(self,storage):
        super().__init__()
        self.storage = storage
        self.results = {}

    def duplicate_analysis(self):
        logger.info(f"executing duplicate_analysis....")
        total_rows = self.storage.data.shape[0]
        duplicate_row =self.storage.data.duplicated().sum()
        output = {
            "No of duplicate rows":duplicate_row,
            "Duplicate row percentage":duplicate_row/total_rows*100
        }
        return output

    def missing_analysis(self):
        logger.info(f"executing missing_analysis....")
        no_of_missing_rows = self.storage.data.isnull().any(axis=1).sum()
        total_rows = self.storage.data.shape[0]
        column_wise_null_count = self.storage.data.isnull().sum().to_dict()
        output = {
            "Total rows containing missing value":no_of_missing_rows,
            "Missing row percentage": no_of_missing_rows/total_rows*100,
            "Missing value per columns": column_wise_null_count
        }
        return output

    def column_stats(self, column=None):
        logger.info(f"executing column_stats over {column}....")
        if column is None:
            raise ValueError("Please provide a column name.")

        col = self.storage.data.get(column)
        if col is None:
            raise ValueError("The column does not exist.")
        output = col.describe().to_dict()
        return output

    def summary(self):
        logger.info(f"executing summary....")
        output = {
            "Rows":self.storage.data.shape[0],
            "Columns":self.storage.data.shape[1],
            "Data type":self.storage.data.dtypes,
            "Memory usage(Bytes)":self.storage.data.memory_usage(deep=True).sum(),
            "Missing values":self.storage.data.isnull().sum().to_dict()
        }
        return output

    def groupby_analysis(self,group_col,agg_col,agg_func,dropna = True):
        logger.info(f"executing groupby_analysis....")
        if group_col or agg_col or agg_func is None:
            raise ValueError("Please provide a column name or a function.")
        output = self.storage.data.groupby(group_col,dropna)[agg_col].agg(agg_func).to_dict()
        return output

    def profile(self):
        logger.info(f"executing profile....")
        missing_report = self.missing_analysis()
        duplicate_report = self.duplicate_analysis()
        output = {
            "generated_at": datetime.now().isoformat(),
            "dataset_info": self.summary(),
            "missing_values": missing_report,
            "duplicate_values": duplicate_report,
            "numeric_columns": self.storage.data.select_dtypes(include=['number']).describe().to_dict(),
            "categorical_columns": self.storage.data.select_dtypes( include=['object', 'category','string']).describe().to_dict(),
            "quality_report":{
                "missing_percentage":missing_report["Missing row percentage"],
                "duplicate_percentage":duplicate_report["Duplicate row percentage"],
            }
        }

        return output

    def run(self, contexts: list[dict]):
        try:
            for context in contexts:
                function = getattr(self, str(context["function"]))
                params = context.get("params", {})
                self.results[str(context["task"])] = function(**params)
        except Exception as e:
            logger.error(f"{e},under Data Analytics Job")
            raise
