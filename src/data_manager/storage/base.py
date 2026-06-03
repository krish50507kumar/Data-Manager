from abc import ABC, abstractmethod
class BaseStorage(ABC):
    """
    Abstract base class for all storage backends.
    Defines the standard interface for loading, writing, and storing data.
    """
    def __init__(self):
        """Initializes the BaseStorage instance."""
        pass
    @abstractmethod
    def load(self, path):
        """
        Loads data from a specified file path.

        Args:
            path (str): The file path to read the data from.
        """
        pass
    @abstractmethod
    def write(self, path):
        """
        Writes the currently stored data to a specified file path.

        Args:
            path (str): The file path to write the data to.
        """
        pass
    @abstractmethod
    def store(self, data):
        """
        Stores data in memory within the storage instance.

        Args:
            data (Any): The data object (e.g., DataFrame) to store.
        """
        pass
