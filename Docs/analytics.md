# Data Analytics

The `DataAnalytics` job generates descriptive statistics, evaluates data quality, and performs aggregations to provide insights into the dataset.

## Core Methods
* **`profile()`**: Compiles a comprehensive report encompassing dataset shape, memory usage, duplicate/missing percentages, and type-specific distributions.
* **`summary()`**: Returns basic structural metadata (rows, columns, dtypes).
* **`duplicate_analysis()` / `missing_analysis()`**: Computes exact counts and overall percentages of bad data.
* **`column_stats(column)`**: Provides standard statistical descriptions (count, mean, std, min, max) for a targeted column.
* **`groupby_analysis(group_col, agg_col, agg_func)`**: Executes dynamic group-by aggregations using specified columns and functions.