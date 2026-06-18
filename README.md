# Data Manager

[![PyPI version](https://img.shields.io/pypi/v/data-manager-framework.svg)](https://pypi.org/project/data-manager-framework/)
[![Python Versions](https://img.shields.io/pypi/pyversions/data-manager-framework.svg)](https://pypi.org/project/data-manager-framework/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Data--Manager-blue?logo=github)](https://github.com/krish50507kumar/Data-Manager)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/data-manager-framework?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/data-manager-framework)

**Data Manager** is a modular Python framework for data engineering, validation, and analytics workflows. It provides a unified, job-based architecture on top of interchangeable storage backends, enabling structured and reproducible processing of tabular datasets.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Architecture Overview](#architecture-overview)
- [Quick Start](#quick-start)
- [Storage Backends](#storage-backends)
  - [CSVStorage](#csvstorage)
  - [JSONStorage](#jsonstorage)
  - [InMemoryStorage](#inmemorystorage)
- [Jobs](#jobs)
  - [DataEngineer](#dataengineer)
  - [DataValidation](#datavalidation)
  - [DataAnalytics](#dataanalytics)
- [Example Pipeline](#example-pipeline)
- [Running Tests](#running-tests)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Pluggable storage backends** — swap between CSV, JSON, and in-memory storage with a consistent interface
- **Job-based execution model** — cleanly separates engineering, validation, and analytics concerns
- **Data engineering utilities** — remove duplicates, handle missing values
- **Data validation** — schema validation, data type checks, and nullability checks
- **Data analytics & profiling** — summary statistics, column-level analysis, missing value reports, and full dataset profiling
- **Fully tested** — comprehensive test suite using `pytest` with coverage reporting

---

## Installation

Install from PyPI:

```bash
pip install data-manager-framework
```

**Requirements:** Python ≥ 3.12, `pandas`, `numpy`

---

## Architecture Overview

Data Manager is built around two core concepts:

1. **Storage Backends** — responsible for reading, holding, and writing data. All backends expose a consistent interface (`read`, `write`, `data`), so jobs are fully decoupled from the underlying file format.

2. **Jobs** — stateless workers that accept a storage object and operate on its data. The three built-in job classes are `DataEngineer`, `DataValidation`, and `DataAnalytics`.

```
┌─────────────────────────────────────────────────────┐
│                    Your Application                  │
└──────────────────────────┬──────────────────────────┘
                           │
              ┌────────────▼────────────┐
              │     Storage Backend     │
              │  CSVStorage             │
              │  JSONStorage            │
              │  InMemoryStorage        │
              └────────────┬────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
┌────────▼───────┐ ┌───────▼──────┐ ┌───────▼────────┐
│  DataEngineer  │ │DataValidation│ │ DataAnalytics  │
│  - duplicates  │ │  - schema    │ │  - summary     │
│  - null values │ │  - types     │ │  - profiling   │
└────────────────┘ │  - nulls     │ │  - statistics  │
                   └──────────────┘ └────────────────┘
```

---

## Quick Start

```python
from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_analytics import DataAnalytics

# Load data
storage = CSVStorage()
storage.load("data.csv")

# Run analytics
analytics = DataAnalytics(storage)
print(analytics.summary())
```

---

## Storage Backends

All storage backends share the same interface. You can swap one for another without changing any of your job code.

### CSVStorage

Reads and writes CSV files using `pandas`.

```python
from data_manager.storage.csv_backend import CSVStorage

storage = CSVStorage()
storage.load("data.csv")

# Access the underlying DataFrame
print(storage.data.head())

# Write back to disk
storage.write("output.csv")
```

### JSONStorage

Reads and writes JSON files.

```python
from data_manager.storage.json_backend import JSONStorage

storage = JSONStorage()
storage.load("data.json")
storage.write("output.json")
```

### InMemoryStorage

Holds data in memory — useful for testing or for passing a pre-built `pandas` DataFrame directly into the job pipeline.

```python
import pandas as pd
from data_manager.storage.In_memory_backend import InMemoryStorage

df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})

storage = InMemoryStorage()
storage.data = df
```

---

## Jobs

Jobs accept a storage object in their constructor and operate on `storage.data`. They do not read or write files themselves — that is the storage layer's responsibility.

### DataEngineer

Handles data cleaning and preprocessing tasks.

```python
from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_engineer import DataEngineer

storage = CSVStorage()
storage.load("raw_data.csv")

engineer = DataEngineer(storage)

# Remove duplicate rows
engineer.removeDuplicates()

# Drop rows with any null values
engineer.removeNull()

# Persist the cleaned dataset
storage.write("cleaned_data.csv")
```

| Method | Description |
|---|---|
| `removeDuplicates()` | Drops all fully duplicate rows from the dataset |
| `removeNull()` | Drops all rows containing one or more null values |

---

### DataValidation

Validates the structure and content of a dataset against expected rules.

```python
from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_validator import DataValidator

storage = CSVStorage()
storage.load("data.csv")

validator = DataValidator(storage)

# Check for required columns and expected types
validator.validateSchema({"name": "object", "age": "int64", "salary": "float64"})

# Check that specific columns have no null values
validator.checkNullability(["name", "age"])
```

| Method | Description |
|---|---|
| `validateSchema(schema)` | Validates that columns exist and match their expected dtypes |
| `checkNullability(columns)` | Raises or reports when specified columns contain null values |

---

### DataAnalytics

Profiles and summarises a loaded dataset.

```python
from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_analytics import DataAnalytics

storage = CSVStorage()
storage.load("data.csv")

analytics = DataAnalytics(storage)

# High-level dataset summary (shape, dtypes, null counts)
print(analytics.summary())

# Per-column descriptive statistics
print(analytics.columnStats())

# Count and percentage of missing values per column
print(analytics.missingValueAnalysis())

# Count and percentage of duplicate rows
print(analytics.duplicateAnalysis())

# Full dataset profile combining all of the above
print(analytics.profile())
```

| Method | Description |
|---|---|
| `summary()` | Returns shape, column names, dtypes, and null counts |
| `columnStats()` | Returns descriptive statistics for each column |
| `missingValueAnalysis()` | Returns missing value counts and percentages per column |
| `duplicateAnalysis()` | Returns the number and percentage of duplicate rows |
| `profile()` | Returns a comprehensive profile of the entire dataset |

---

## Example Pipeline

The following example shows a complete end-to-end workflow — loading raw data, cleaning it, validating it, and profiling the result.

```python
from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_engineer import DataEngineer
from data_manager.jobs.data_validator import DataValidator
from data_manager.jobs.data_analytics import DataAnalytics

# --- Step 1: Load ---
storage = CSVStorage()
storage.load("raw_data.csv")

# --- Step 2: Engineer ---
engineer = DataEngineer(storage)
engineer.removeDuplicates()
engineer.removeNull()

# --- Step 3: Validate ---
validator = DataValidator(storage)
validator.validateSchema({"name": "object", "age": "int64"})
validator.checkNullability(["name"])

# --- Step 4: Analyse ---
analytics = DataAnalytics(storage)
print(analytics.profile())

# --- Step 5: Save ---
storage.write("cleaned_data.csv")
```

---

## Running Tests

The full test suite is written with `pytest` and includes coverage reporting.

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run with coverage report:

```bash
pytest --cov=data_manager
```

---

## Roadmap

| Status | Feature |
|---|---|
| ✅ Done | CSV Backend |
| ✅ Done | JSON Backend |
| ✅ Done | In-Memory Backend |
| ✅ Done | Data Validation |
| ✅ Done | Data Analytics & Profiling |
| 🔲 Planned | Excel Backend |
| 🔲 Planned | Parquet Backend |
| 🔲 Planned | SQL Backend |
| 🔲 Planned | Automated EDA Reports |

---

## Contributing

Contributions are welcome. To get started:

1. Fork the repository on GitHub.
2. Clone your fork and create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Install the project in editable mode:
   ```bash
   pip install -e .
   ```
4. Make your changes and ensure all tests pass:
   ```bash
   pytest -v
   ```
5. Open a pull request against the `main` branch with a clear description of your changes.

Please keep pull requests focused and scoped to a single concern. Bug fixes, new storage backends, and additional job methods are all welcome.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Author

**Krish Kumar** — [GitHub](https://github.com/krish50507kumar)