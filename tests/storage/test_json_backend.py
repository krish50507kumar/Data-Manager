import pytest
import pandas as pd
from data_manager.storage.json_backend import JSONStorage


@pytest.fixture
def storage():
    return JSONStorage()

def test_store(storage):
    data = [
        {"name": "Alice", "age": 20},
        {"name": "Bob", "age": 21}
    ]

    storage.store(data)

    assert storage.data is not None
    assert len(storage.data) == 2
    assert list(storage.data.columns) == ["name", "age"]




def test_load(storage, tmp_path):
    df = pd.DataFrame({
        "name": ["Alice"],
        "age": [20]
    })

    json_file = tmp_path / "test.json"

    df.to_json(json_file)

    storage.load(json_file)

    assert storage.data is not None
    assert len(storage.data) == 1
    assert storage.path == json_file




def test_load_invalid_path(storage):
    with pytest.raises(FileNotFoundError):
        storage.load("does_not_exist.json")



def test_write(storage, tmp_path):
    storage.data = pd.DataFrame({
        "name": ["Alice"],
        "age": [20]
    })

    output_file = tmp_path / "output.json"

    storage.write(output_file)

    assert output_file.exists()




def test_write_uses_stored_path(storage, tmp_path):
    output_file = tmp_path / "output.json"

    storage.path = output_file

    storage.data = pd.DataFrame({
        "x": [1, 2]
    })

    storage.write(None)

    assert output_file.exists()




def test_json_round_trip(storage, tmp_path):
    original = pd.DataFrame({
        "name": ["Alice", "Bob"],
        "age": [20, 21]
    })

    storage.data = original

    json_file = tmp_path / "roundtrip.json"

    storage.write(json_file)

    loaded = JSONStorage()
    loaded.load(json_file)

    assert len(loaded.data) == len(original)
    assert list(loaded.data.columns) == list(original.columns)