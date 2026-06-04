# Data Manager

A modular Python framework for data engineering, validation, and analytics workflows.

Data Manager provides a job-based architecture and pluggable storage backends for processing tabular datasets in a structured and extensible way.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Features

* Modular storage backends (CSV, JSON, In-Memory)
* Job-based execution architecture
* Data engineering utilities
* Data validation and schema checking
* Data analytics and profiling
* Fully tested with Pytest

---

## Installation

```bash
pip install data-manager-framework
```

---

## Quick Start

```python
from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_analytics import DataAnalytics

storage = CSVStorage()
storage.read("data.csv")

analytics = DataAnalytics(storage)

print(analytics.summary())
```

---

## Core Components

### Storage Layer

Provides interchangeable storage backends:

* CSVStorage
* JSONStorage
* InMemoryStorage

### Data Engineering

Available operations:

* Remove duplicate records
* Handle missing values

### Data Validation

Available validations:

* Schema validation
* Data type checks
* Nullability checks

### Data Analytics

Available analytics:

* Dataset summary
* Column statistics
* Missing value analysis
* Duplicate analysis
* Dataset profiling

---

## Example Pipeline

```python
from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_engineer import DataEngineer

storage = CSVStorage()
storage.read("data.csv")

engineer = DataEngineer(storage)

engineer.removeDuplicates()
engineer.removeNull()

storage.write("cleaned_data.csv")
```

---

## Testing

Run the complete test suite:

```bash
pytest
```

Verbose mode:

```bash
pytest -v
```

---

## Current Capabilities

| Component   | Features                                                      |
| ----------- | ------------------------------------------------------------- |
| Storage     | CSV, JSON, In-Memory                                          |
| Engineering | Remove duplicates, Handle missing values                      |
| Validation  | Schema validation, Nullability checks                         |
| Analytics   | Summary, Profiling, Missing value analysis, Column statistics |

---

## Roadmap

* [x] CSV Backend
* [x] JSON Backend
* [x] In-Memory Backend
* [x] Data Validation
* [x] Data Analytics
* [ ] Excel Backend
* [ ] Parquet Backend
* [ ] SQL Backend
* [ ] Automated EDA Reports

---

## License

MIT License

---

## Author

Krish Kumar
