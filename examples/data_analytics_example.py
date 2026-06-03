
from data_manager.storage.csv_backend import CSVStorage
from data_manager.jobs.data_engineer import DataEngineer
from data_manager.jobs.data_analytics import DataAnalytics
import pandas as pd
data_path = "../tests/data/test_data_1.csv"
MyStorage = CSVStorage()
df = pd.DataFrame()
MyStorage.store(df)

MyDataEngineer = DataEngineer(MyStorage)

DataEngineerContext = [
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

MyDataEngineer.run(DataEngineerContext)

MyDataAnalytics = DataAnalytics(MyStorage)

DataAnalyticsContext = [
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

MyDataAnalytics.run(DataAnalyticsContext)

# print(MyDataAnalytics.results.get("Summary_of_the_data"))
# print(MyDataAnalytics.results.get("Checking_name_column"))
# print(MyDataAnalytics.results.get("Data_profile"))

MyStorage.write(path ="../tests/data/test_data_3.csv")

print("THE END")