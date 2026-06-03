import numpy as np

from data_manager.core.base_job import BaseJob
import pandas as pd
from pandas.api.types import (
    is_string_dtype,
    is_numeric_dtype,
    is_integer_dtype,
    is_float_dtype
)
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("DataManager")

class DataValidator(BaseJob):
    def __init__(self,storage):
        super().__init__()
        self.storage = storage
        self.results = {}

    def validate_schema(self, schema):
        logger.info("Validating schema....")

        valid = True
        errors = {}

        for col, constraints in schema.items():

            if col not in self.storage.data.columns:
                errors[col] = "Column not found"
                valid = False
                continue

            series = self.storage.data[col]

            nullable = constraints.get("nullable", True)

            if not nullable:
                null_count = series.isnull().sum()

                if null_count > 0:
                    errors[col] = f"Contains {null_count} null values"
                    valid = False
                    continue

            expected_dtype = constraints.get("dtype")

            if expected_dtype is None:
                continue

            dtype_valid = True

            if expected_dtype == str:
                dtype_valid = is_string_dtype(series)

            elif expected_dtype == int:
                dtype_valid = is_integer_dtype(series)

            elif expected_dtype == float:
                dtype_valid = is_float_dtype(series)

            elif expected_dtype == np.number:
                dtype_valid = is_numeric_dtype(series)


            elif expected_dtype == object:
                dtype_valid = is_string_dtype(series)

            else:
                errors[col] = f"Unsupported dtype: {expected_dtype}"
                valid = False
                continue

            if not dtype_valid:
                errors[col] = (
                    f"Expected {expected_dtype.__name__}, "
                    f"found {series.dtype}"
                )
                valid = False
        return {
            "valid": valid,
            "errors": errors
        }



    def run(self, contexts: list[dict]):
        try:
            for context in contexts:
                function = getattr(self, str(context["function"]))
                params = context.get("params", {})
                self.results[str(context["task"])] = function(**params)
        except Exception as e:
            logger.error(f"{e},under Data Validator Job")