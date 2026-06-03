import pytest
import pandas as pd

from data_manager.storage.csv_backend import CSVStorage


@pytest.fixture
def sample_storage():
    storage = CSVStorage()

    storage.data = pd.DataFrame({
        "name": ["Alice", "Bob", "Bob", None],
        "age": [20, 21, 21, None],
        "salary": [50000, 60000, 60000, None]
    })

    return storage