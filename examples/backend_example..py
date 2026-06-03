"""
all backends have same api's
"""
from data_manager.storage.csv_backend import CSVStorage
import pandas as pd
# EXAMPLE 1
storage_1 = CSVStorage() # create a storage
test_data_path = "../tests/data/test_data_1.csv"
storage_1.load(test_data_path)
# some job operation in between
storage_1.write() # save you change either at new location or same location

# EXAMPLE 2
storage_2 = CSVStorage()
df = pd.DataFrame({
    "name":["john","ram","dany",None],
    "age":[20, 30, 40, 50],
})
storage_2.store(df) # stores your dataframe data
yourpath = "../tests/data/test_data_3.csv"
storage_2.write(path=yourpath) # save your data at any location