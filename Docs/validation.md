# Data Validation

The `DataValidator` job ensures the integrity of the dataset by checking it against strict, predefined schemas before it enters analytical or engineering pipelines.

## Core Methods
* **`validate_schema(schema)`**: Evaluates the DataFrame against a dictionary defining column constraints.
  * **Supported Constraints**: Evaluates column existence, nullability (`nullable: bool`), and data types (e.g., `str`, `int`, `float`, `object`).
  * **Output**: Returns a dictionary containing a `valid` boolean flag and an `errors` object that details exactly which columns failed and why.