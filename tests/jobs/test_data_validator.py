import pytest
import pandas as pd

from data_manager.storage.csv_backend import CSVStorage


@pytest.fixture
def valid_storage():
    storage = CSVStorage()

    storage.dd = pd.DataFrame({
        "name": ["Alice", "Bob"],
        "age": [20, 21],
        "salary": [50000.0, 60000.0]
    })

    return storage


from data_manager.jobs.data_validator import DataValidator


def test_validate_schema_valid(valid_storage):
    validator = DataValidator(valid_storage)

    schema = {
        "name": {
            "dtype": object,
            "nullable": False
        },
        "age": {
            "dtype": int,
            "nullable": False
        }
    }

    result = validator.validate_schema(schema)

    assert result["valid"] is True
    assert result["errors"] == {}

def test_validate_schema_missing_column(valid_storage):
    validator = DataValidator(valid_storage)

    schema = {
        "email": {
            "dtype": object,
            "nullable": False
        }
    }

    result = validator.validate_schema(schema)

    assert result["valid"] is False
    assert "email" in result["errors"]

def test_validate_schema_nulls():
    storage = CSVStorage()

    storage.dd = pd.DataFrame({
        "name": ["Alice", None]
    })

    validator = DataValidator(storage)

    schema = {
        "name": {
            "dtype": object,
            "nullable": False
        }
    }

    result = validator.validate_schema(schema)

    assert result["valid"] is False
    assert "null" in result["errors"]["name"].lower()

def test_validate_schema_wrong_dtype(valid_storage):
    validator = DataValidator(valid_storage)

    schema = {
        "age": {
            "dtype": str,
            "nullable": False
        }
    }

    result = validator.validate_schema(schema)

    assert result["valid"] is False
    assert "age" in result["errors"]

def test_validate_schema_nullable_allowed():
    storage = CSVStorage()

    storage.dd = pd.DataFrame({
        "name": ["Alice", None]
    })

    validator = DataValidator(storage)

    schema = {
        "name": {
            "dtype": object,
            "nullable": True
        }
    }

    result = validator.validate_schema(schema)

    assert result["valid"] is True


def test_run_validator(valid_storage):
    validator = DataValidator(valid_storage)

    context = [
        {
            "task": "schema_check",
            "function": "validate_schema",
            "params": {
                "schema": {
                    "age": {
                        "dtype": int,
                        "nullable": False
                    }
                }
            }
        }
    ]

    validator.run(context)

    assert "schema_check" in validator.results

def test_run_invalid_function(caplog, valid_storage):
    validator = DataValidator(valid_storage)

    context = [
        {
            "task": "bad",
            "function": "does_not_exist",
            "params": {}
        }
    ]

    validator.run(context)

    assert "does_not_exist" in caplog.text

def test_validate_empty_schema(valid_storage):
    validator = DataValidator(valid_storage)

    result = validator.validate_schema({})

    assert result["valid"] is True
    assert result["errors"] == {}