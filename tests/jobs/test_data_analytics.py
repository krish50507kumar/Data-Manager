from data_manager.jobs.data_analytics import DataAnalytics
import pandas as pd
from data_manager.storage.csv_backend import CSVStorage
import pytest

def test_summary_returns_dict(sample_storage):
    analytics = DataAnalytics(sample_storage)

    result = analytics.summary()

    assert isinstance(result, dict)


def test_summary_empty_dataframe():
    storage = CSVStorage()
    storage.data = pd.DataFrame()

    analytics = DataAnalytics(storage)

    result = analytics.summary()

    assert result is not None

def test_column_stats_numeric_column(sample_storage):
    analytics = DataAnalytics(sample_storage)

    result = analytics.column_stats("age")

    assert isinstance(result, dict)
    assert "count" in result

def test_column_stats_string_column(sample_storage):
    analytics = DataAnalytics(sample_storage)

    result = analytics.column_stats("name")

    assert isinstance(result, dict)
    assert "count" in result

def test_column_stats_invalid_column(sample_storage):
    analytics = DataAnalytics(sample_storage)

    with pytest.raises(ValueError):
        analytics.column_stats("fake_column")



def test_column_stats_empty_column(sample_storage):
    analytics = DataAnalytics(sample_storage)

    with pytest.raises(Exception):
        analytics.column_stats("")

def test_missing_analysis(sample_storage):
    analytics = DataAnalytics(sample_storage)

    result = analytics.missing_analysis()

    assert isinstance(result, dict)



def test_missing_analysis_no_nulls():
    storage = CSVStorage()

    storage.data = pd.DataFrame({
        "a": [1, 2],
        "b": [3, 4]
    })

    analytics = DataAnalytics(storage)

    result = analytics.missing_analysis()

    assert result is not None

def test_duplicate_analysis(sample_storage):
    analytics = DataAnalytics(sample_storage)

    result = analytics.duplicate_analysis()

    assert result is not None



def test_duplicate_analysis_no_duplicates():
    storage = CSVStorage()

    storage.data = pd.DataFrame({
        "id": [1, 2, 3]
    })

    analytics = DataAnalytics(storage)

    result = analytics.duplicate_analysis()

    assert result is not None

def test_profile(sample_storage):
    analytics = DataAnalytics(sample_storage)

    result = analytics.profile()

    assert isinstance(result, dict)

def test_profile_contains_sections(sample_storage):
    analytics = DataAnalytics(sample_storage)

    result = analytics.profile()
    assert "generated_at" in result
    assert "dataset_info" in result
    assert "missing_values" in result
    assert "duplicate_values" in result
    assert "numeric_columns" in result
    assert "categorical_columns" in result
    assert "quality_report" in result

def test_run_pipeline(sample_storage):
    analytics = DataAnalytics(sample_storage)

    context = [
        {
            "task": "summary_task",
            "function": "summary",
            "params": {}
        },
        {
            "task": "stats_task",
            "function": "column_stats",
            "params": {
                "column": "age"
            }
        }
    ]

    analytics.run(context)

    assert "summary_task" in analytics.results
    assert "stats_task" in analytics.results

import pytest


def test_run_invalid_function_logs_error(sample_storage, caplog):
    analytics = DataAnalytics(sample_storage)

    context = [
        {
            "task": "bad",
            "function": "does_not_exist",
            "params": {}
        }
    ]

    analytics.run(context)

    assert "under Data Analytics Job" in caplog.text