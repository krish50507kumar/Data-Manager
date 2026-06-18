# Execution Runner

The `Runner` acts as the central orchestrator for the Data Manager framework. Instead of manually invoking methods on job classes, workflows are defined as a list of tasks and passed to the Runner.

## Usage
Workflows are structured as a list of dictionaries, mapping a `job` instance to its execution `contexts`.
```python
runner = Runner(works=[
    {
        "job": data_engineer_instance,
        "contexts": [{"function": "removeDuplicates"}]
    }
])
runner.run()