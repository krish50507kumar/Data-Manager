from data_manager.storage.base import BaseStorage
import pandas as pd
from pathlib import Path
class CSVStorage(BaseStorage):
    """
        Storage backend for handling CSV files.
        """
    def __init__(self):
        """Initializes the CSVStorage instance with empty data and path."""
        super().__init__()
        self.data = None
        self.path = None | str
    def store(self, data):
        """
        Stores a pandas DataFrame in the instance.

        Args:
            data (pd.DataFrame): The DataFrame to store.
        """
        self.data = data
    def load(self, path):
        """
        Loads a CSV file into a pandas DataFrame.

        Args:
            path (str): The path to the CSV file.
        """
        self.path = path
        self.data = pd.read_csv(self.path)
    def write(self,path=None):
        """
        Writes the stored DataFrame to a CSV file.

        Args:
            path (str, optional): The destination path. If None, uses the loaded path.
        """
        path = path if path is not None else self.path
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        self.data.to_csv(file_path, index=False)

