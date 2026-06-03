import pandas as pd
from data_manager.storage.base import BaseStorage
import logging
from pathlib import Path
logger = logging.getLogger("DataManager")

class InMemoryStorage(BaseStorage):
    """
    Storage backend for handling in-memory pandas DataFrames.
    """
    def __init__(self):
        """Initializes the InMemoryStorage instance."""
        super().__init__()
        self.path: str | None = None
        self.data: pd.DataFrame | None = None

    def load(self, path: str) -> None:
        """
        Loads data from a CSV file path into memory.

        Args:
            path (str): The file path to load data from.
        """
        self.path = path
        self.data = pd.read_csv(path)
        logger.info(f"Loaded {len(self.data)} rows from {path}")

    def write(self, path: str) -> None:
        """
        Writes the in-memory DataFrame to a CSV file.

        Args:
            path (str): The destination file path.

        Raises:
            ValueError: If no data is currently stored in memory.
        """
        path = path if path is not None else self.path
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if self.data is None:
            raise ValueError("No data to write. Call store() or load() first.")
        self.data.to_csv(file_path, index=False)
        logger.info(f"Written {len(self.data)} rows to {file_path}")

    def store(self, data: pd.DataFrame) -> None:
        """
        Directly stores a pandas DataFrame in memory.

        Args:
            data (pd.DataFrame): The DataFrame to store.

        Raises:
            TypeError: If the provided data is not a pandas DataFrame.
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError(f"Expected a pandas DataFrame, got {type(data).__name__}")
        self.data = data
        logger.info(f"Stored DataFrame with {len(self.data)} rows in memory")
