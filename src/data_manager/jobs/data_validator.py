import numpy as np

from src.data_manager.core.base_job import BaseJob
import pandas as pd
class DataValidator(BaseJob):
    def __init__(self,data):
        super().__init__()
        self.data = data

    def validate_schema(self, schema):
        valid = True
        errors = {}

        for col, constraints in schema.items():
            # 1. Check if column exists
            if col not in self.data.dd.columns:
                errors[col] = "Column not found"
                valid = False
                continue

            # 2. Check for null values
            if not constraints.get("nullable", True):
                null_count = self.data.dd[col].isnull().sum()
                if null_count > 0:
                    errors[col] = f"Contains {null_count} null values"
                    valid = False
                    continue

            # 3. Check data types
            expected_dtype = constraints["dtype"]
            actual_dtype = self.data.dd[col].dtype

            # Simplified type checking
            if not np.issubdtype(actual_dtype, expected_dtype):
                errors[col] = f"Expected {expected_dtype.__name__}, found {actual_dtype}"
                valid = False

            # 4. Check for non-numeric values (if expecting numeric)
            if expected_dtype in [int, float, np.number]:
                if not pd.api.types.is_numeric_dtype(self.data.ddf[col]):
                    errors[col] = "Contains non-numeric values"
                    valid = False

        return {"valid": valid, "errors": errors}


    def run(self, contexts: list[dict]):
        for context in contexts:
            function = getattr(self, str(context["function"]))
            params = context.get("params", {})
            function(**params)