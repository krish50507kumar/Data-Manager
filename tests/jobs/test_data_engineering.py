import pytest
import pandas as pd
from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_engineer import DataEngineer

def test_remove_duplicates():
    storage = CSVStorage()

    storage.data = pd.DataFrame({
        "id": [1, 1, 2]
    })

    engineer = DataEngineer(storage)

    engineer.removeDuplicates()

    assert len(storage.data) == 2

def test_removeNull():
    storage = CSVStorage()

    storage.data = pd.DataFrame({
        "id": [1, None, 2]
    })

    engineer = DataEngineer(storage)

    engineer.removeNull()
    assert len(storage.data) == 2

