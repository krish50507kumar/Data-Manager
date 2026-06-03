from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_engineer import DataEngineer

data_storage = CSVStorage()
test_data_path ="../tests/data/test_data_1.csv"
data_storage.load(test_data_path)

data_engineer_job = DataEngineer(data_storage)

# process


data_engineer_job.removeDuplicates()
data_engineer_job.removeNull()

"""
OR
data_engineer_tasks = [
    {
        "function": "removeDublicate",
        "params": {}
    },
    {
        "function": "removeNull",
        "params": {
            "method" : "drop"
        }
    }
]
data_engineer_job.run(data_engineer_tasks)
"""


# SAVE YOUR MODIFOED DATA
data_storage.write(test_data_path)
