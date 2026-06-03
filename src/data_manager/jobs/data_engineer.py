import numpy as np
import logging


from data_manager.core.base_job import BaseJob
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("DataManager")

class DataEngineer(BaseJob):
    def __init__(self,storage):
        super().__init__()
        self.storage = storage

    def removeDuplicates(self):
        logger.info(f"executing removeDuplicates....")
        before = self.storage.data.shape[0]
        self.storage.data.drop_duplicates(inplace=True)
        after = self.storage.data.shape[0]
        logger.info(f"{before-after} duplicate rows removed")

    def removeNull(self,method = "drop",num_const = 0,category_const ="Unknown" ):
        logger.info(f"executing removeNull....")
        if method == "drop":
            before = self.storage.data.shape[0]
            self.storage.data.dropna(inplace=True)
            after = self.storage.data.shape[0]
            logger.info(f"{before-after} null rows dropped")
        elif method == "const":
            total_null = self.storage.data.isnull().any(axis=1).sum()
            numericCols = self.storage.data.select_dtypes(include=np.number).columns
            objectCols = self.storage.data.select_dtypes(exclude=np.number).columns
            self.storage.data[numericCols] = self.storage.data[numericCols].fillna(num_const)
            self.storage.data[objectCols] = self.storage.data[objectCols].fillna(category_const)
            logger.info(f"{total_null} null values are filled")
        else :
            raise ValueError("Invalid method")

    def run(self, contexts: list[dict]):
        try:
            for context in contexts:
                function = getattr(self, str(context["function"]))
                params = context.get("params", {})
                function(**params)
        except Exception as e:
            logger.error(f"{e},under Data Engineer Job")

