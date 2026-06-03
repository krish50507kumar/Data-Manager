from data_manager.storage.base import BaseStorage
import pandas as pd
class JSONStorage(BaseStorage):
    """
    Storage backend for handling JSON files.
    """
    def __init__(self):
        """Initializes the JSONStorage instance with empty data and path."""
        super().__init__()
        self.data=None
        self.path = None
    def load(self, path):
        """
        Loads a JSON file into a pandas DataFrame.

        Args:
            path (str): The path to the JSON file.
        """
        self.path = path
        self.data = pd.read_json(path)
    def write(self,path):
        """
        Writes the stored DataFrame to a JSON file.

        Args:
            path (str): The destination path. If None, uses the loaded path.
        """
        path = path if path is not None else self.path
        self.data.to_json(path, index=False)
    def store(self, data):
        """
        Stores raw data by converting it into a pandas DataFrame.

        Args:
            data (list/dict/etc): The data to convert and store.
        """
        self.data = pd.DataFrame(data)