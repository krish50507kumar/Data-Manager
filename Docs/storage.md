# Storage Backend

The storage layer provides a unified interface (`BaseStorage`) for data I/O, allowing jobs to process data without knowing its origin. 

## Supported Backends
* **CSVStorage**: Reads and writes `.csv` files.
* **JSONStorage**: Reads and writes `.json` files.
* **InMemoryStorage**: Handles direct Pandas DataFrame injection for temporary or high-speed pipelines.

## Core Methods
* `load(path)`: Reads data from the specified path into the backend instance.
* `write(path)`: Saves the currently held DataFrame to the specified path.
* `store(data)`: Explicitly assigns a raw DataFrame or dictionary into the backend's memory.