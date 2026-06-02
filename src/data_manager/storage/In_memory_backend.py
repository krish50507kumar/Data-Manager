import pandas as pd
from data_manager.storage.base import BaseStorage
import logging

logger = logging.getLogger("DataManager")

class InMemoryStorage(BaseStorage):
    def __init__(self):
        super().__init__()
        self.path: str | None = None
        self.dd: pd.DataFrame | None = None

    def load(self, path: str) -> None:
        self.path = path
        self.dd = pd.read_csv(path)
        logger.info(f"Loaded {len(self.dd)} rows from {path}")

    def write(self, path: str) -> None:
        if self.dd is None:
            raise ValueError("No data to write. Call store() or load() first.")
        self.dd.to_csv(path, index=False)
        logger.info(f"Written {len(self.dd)} rows to {path}")

    def store(self, data: pd.DataFrame) -> None:
        if not isinstance(data, pd.DataFrame):
            raise TypeError(f"Expected a pandas DataFrame, got {type(data).__name__}")
        self.dd = data
        logger.info(f"Stored DataFrame with {len(self.dd)} rows in memory")
