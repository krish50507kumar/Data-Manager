import pandas as pd
from data_manager.jobs.data_validator import DataValidator
from data_manager.storage.csv_backend import CSVStorage

df = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 28, 35],
    "salary": [50000, 60000, 55000, 70000],
    "email": [
        "alice@example.com",
        "bob@example.com",
        "charlie@example.com",
        "david@example.com"
    ]
})

schema = {
    "id": {
        "dtype": "int64",
        "nullable": False
    },
    "name": {
        "dtype": "object",
        "nullable": False
    },
    "age": {
        "dtype": "int64",
        "nullable": False,
    },
    "salary": {
        "dtype": "int64",
        "nullable": False,
    },
    "email": {
        "dtype": "object",
        "nullable": False
    }
}
storage = CSVStorage()
storage.store(df)
validator = DataValidator(storage)
print(validator.validate_schema(schema))
