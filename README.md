# Data Manager

A modular Python framework for data engineering, validation, and analytics workflows.

DataManager uses a job-based architecture and pluggable storage backends to provide a structured approach for processing tabular datasets.

## Features

* **Modular Storage Backends**: Decoupled storage interfaces allowing seamless switching between In-Memory, CSV, and JSON data layers.
* **Extensible Job Architecture**: Abstracted base classes (`base_job.py`) that make it easy to write custom logic for engineering, validation, and analytics.
* **Comprehensive Test Suite**: Test-driven design featuring deep unit testing and interactive Jupyter Notebooks for debugging and validation.

## System Architecture

The framework is divided into three primary layers:

1. **Storage Layer (`src/data_manager/storage/`)**
* `base.py`: The abstract base class defining standard data operations.
* `csv_backend.py` & `json_backend.py`: File-based storage implementations.
* `In_memory_backend.py`: RAM-based storage for high-speed, temporary data transformations.


2. **Execution Layer (`src/data_manager/jobs/`)**
* `data_engineer.py`: Logic for data cleaning, transformation, and feature engineering.
* `data_validator.py`: Rules and assertions to ensure data quality and schema integrity.
* `data_analytics.py`: Calculation of metrics, aggregations, and business logic.


## Directory Structure

```text
📦 data-manager
 ┣ 📂 Notebooks                 # Exploratory data analysis and experimental workflows
 ┃ ┗ 📜 notes_1.ipynb
 ┣ 📂 src
 ┃ ┗ 📂 data_manager
 ┃   ┣ 📂 config                
 ┃   ┣ 📂 core
 ┃   ┃ ┗ 📜 base_job.py         # Abstract base class for all pipeline jobs
 ┃   ┣ 📂 jobs
 ┃   ┃ ┣ 📜 data_analytics.py   # Analytics and metrics processing
 ┃   ┃ ┣ 📜 data_engineer.py    # ETL and transformation logic
 ┃   ┃ ┗ 📜 data_validator.py   # Data quality assurance
 ┃   ┣ 📂 storage
 ┃   ┃ ┣ 📜 In_memory_backend.py
 ┃   ┃ ┣ 📜 base.py             # Storage interface definitions
 ┃   ┃ ┣ 📜 csv_backend.py
 ┃   ┃ ┗ 📜 json_backend.py
 ┃   ┗ 📜 runner.py             
 ┣ 📂 tests                     # Unit and integration tests (Pytest)
 ┃ ┣ 📂 Data                    # Mock datasets for testing pipelines
 ┃ ┣ 📂 jobs                    # Tests for specific job implementations
 ┃ ┗ 📂 storage                 # Tests for storage backends
 ┣ 📜 main.py                   # Application entry point
 ┣ 📜 conftest.py               # Pytest configuration and fixtures
 ┗ 📜 pytest.ini                # Pytest environment settings

```

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed. It is recommended to use a virtual environment.

```bash
# Clone the repository
git clone https://github.com/krish50507kumar/data-manager.git
cd data-manager

# Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
### Installation

```bash
pip install -r requirements.txt
```
## Quick Start

```python
from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_analytics import DataAnalytics

storage = CSVStorage()
storage.read("data.csv")

analytics = DataAnalytics(storage)

print(analytics.summary())
```

### example

```python

from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_engineer import DataEngineer
from data_manager.jobs.data_analytics import DataAnalytics
import pandas as pd
df = pd.DataFrame()
mystorage = CSVStorage()
mystorage.store(df)

mydataengineer = DataEngineer(mystorage)

dataengineercontext = [
    {
        "task":"removeDuplicates",
        "function":"removeDuplicates",
        "params":{}
    },
    {
        "task":"removeNull",
        "function":"removeNull",
        "params":{
            "method":"const",
            "num_const":0,
            "category_const":"Unknown"
        }
    }
]

mydataengineer.run(dataengineercontext)

mydataanalytics = DataAnalytics(mystorage)

dataanalyticscontext = [
    {
        "task":"Summary_of_the_data",
        "function":"summary",
        "params":{}
    },
    {
        "task":"Checking_name_column",
        "function":"column_stats",
        "params":{
        }
    },
    {
        "task":"Data_profile",
        "function":"profile",
        "params":{}
    },
    {
        "task":"grouping_name_with_salary ",
        "function":"groupby_analysis",
        "params":{}
    }
]

mydataanalytics.run(dataanalyticscontext)

# print(MyDataAnalytics.results.get("Summary_of_the_data"))
# print(MyDataAnalytics.results.get("Checking_name_column"))
# print(MyDataAnalytics.results.get("Data_profile"))

mystorage.write(path = "D:\\workspace\\Dev tools\\PythonProjects\\DataManager\\tests\\Data\\test_data_3.csv")

print("THE END")


```

### Usage

To trigger the data pipelines, execute the main entry point:

```bash
python main.py

```



## Testing

The framework utilizes `pytest` to ensure reliability across all modules. The test suite covers isolated unit tests for storage backends, validation logic, and analytics generation, as well as notebook-based integration tests.

To run the full test suite:

```bash
# Run all tests in the /tests directory
pytest

# Run tests with detailed verbose output
pytest -v

```
## Current Capabilities

| Component | Features |
|------------|------------|
| Storage | CSV, JSON, In-Memory |
| Engineering | Remove duplicates, Handle missing values |
| Validation | Schema validation, Nullability checks |
| Analytics | Summary, Profiling, Missing value analysis, Column statistics |

## Roadmap

- [x] CSV Backend
- [x] JSON Backend
- [x] In-Memory Backend
- [x] Data Validation
- [x] Data Analytics
- [ ] Excel Backend
- [ ] Parquet Backend
- [ ] SQL Backend
- [ ] Automated EDA Reports

---
# Author
### Krish Kumar