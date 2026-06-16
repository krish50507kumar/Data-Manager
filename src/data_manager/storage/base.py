from abc import ABC, abstractmethod

from fontTools.misc import iftSparseBitSet

from data_manager.transactions._savepoint import _Savepoint
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

    def savepoint(self,name):
        self.stack.append(_Savepoint(name))

    def roleback(self):
        if not self.stack :
            return
        sp = self.stack.pop()
        if '__table__' in sp.deltas:
            self.data = sp.deltas['__table__'].copy()
        else:
            for col , old_vals in sp.deltas.items():
                if old_vals is None:
                    self.data.drop(col, inplace=True)
                else:
                   self.data[col] = old_vals
