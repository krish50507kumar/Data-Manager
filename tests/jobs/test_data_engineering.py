import pytest
import pandas as pd
from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_engineer import DataEngineer

def test_remove_duplicates():
    storage = CSVStorage()

    storage.dd = pd.DataFrame({
        "id": [1, 1, 2]
    })

    engineer = DataEngineer(storage)

    engineer.removeDuplicates()

    assert len(storage.dd) == 2

def test_removeNull():
    storage = CSVStorage()

    storage.dd = pd.DataFrame({
        "id": [1, None, 2]
    })

    engineer = DataEngineer(storage)

    engineer.removeNull()
    assert len(storage.dd) == 2

