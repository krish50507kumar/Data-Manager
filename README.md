# Data Manager

A robust, modular Python framework built for orchestrating data pipelines, performing rigorous validations, and executing analytics. Designed with a clean separation of concerns, this project provides a flexible architecture for handling data workflows from ingestion to analysis.

## Features

* **Modular Storage Backends**: Decoupled storage interfaces allowing seamless switching between In-Memory, CSV, and JSON data layers.
* **Pipeline Orchestration**: A dedicated `runner.py` to execute complex data jobs systematically.
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


3. **Orchestration Layer (`src/data_manager/runner.py`)**
* The central engine responsible for loading configurations, initializing the correct storage backend, and sequentially executing the defined jobs.



## Directory Structure

```text
📦 data-manager
 ┣ 📂 Notebooks                 # Exploratory data analysis and experimental workflows
 ┃ ┗ 📜 notes_1.ipynb
 ┣ 📂 src
 ┃ ┗ 📂 data_manager
 ┃   ┣ 📂 config                # Configuration management
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
 ┃   ┗ 📜 runner.py             # Pipeline execution engine
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

### Usage

To trigger the data pipelines, execute the main entry point:

```bash
python main.py

```

*Note: You can adjust the specific workflows, data paths, and storage backends being used by modifying the configuration passed to the `runner.py`.*

## Testing

The framework utilizes `pytest` to ensure reliability across all modules. The test suite covers isolated unit tests for storage backends, validation logic, and analytics generation, as well as notebook-based integration tests.

To run the full test suite:

```bash
# Run all tests in the /tests directory
pytest

# Run tests with detailed verbose output
pytest -v

```

# Author
### Krish Kumar