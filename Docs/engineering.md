# Data Engineering

The `DataEngineer` job handles data cleaning, preprocessing, and transformations. Operations modify the storage backend's DataFrame in-place.

## Core Methods
* **`removeDuplicates()`**: Identifies and drops all duplicate rows from the dataset.
* **`removeNull(method, num_const, category_const)`**: Handles missing values based on the chosen strategy.
  * `method="drop"`: Removes any row containing one or more null values.
  * `method="const"`: Fills missing numeric values with `num_const` (default `0`) and missing categorical/string values with `category_const` (default `"Unknown"`).