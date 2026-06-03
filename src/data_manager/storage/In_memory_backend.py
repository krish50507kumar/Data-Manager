import pandas as pd
from data_manager.storage.base import BaseStorage
import logging

logger = logging.getLogger("DataManager")

class InMemoryStorage(BaseStorage):
    def __init__(self):
        super().__init__()
        self.path: str | None = None
        self.data: pd.DataFrame | None = None

    def load(self, path: str) -> None:
        self.path = path
        self.data = pd.read_csv(path)
        logger.info(f"Loaded {len(self.data)} rows from {path}")

    def write(self, path: str) -> None:
        if self.data is None:
            raise ValueError("No data to write. Call store() or load() first.")
        self.data.to_csv(path, index=False)
        logger.info(f"Written {len(self.data)} rows to {path}")

    def store(self, data: pd.DataFrame) -> None:
        if not isinstance(data, pd.DataFrame):
            raise TypeError(f"Expected a pandas DataFrame, got {type(data).__name__}")
        self.data = data
        logger.info(f"Stored DataFrame with {len(self.data)} rows in memory")
