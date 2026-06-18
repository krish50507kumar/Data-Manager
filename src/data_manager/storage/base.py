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
        """
            Creates a new savepoint and pushes it onto the transaction stack.

            This method allows you to mark a specific state in the data's history
            so that it can be reverted to later using the `rollback` method.

            Args:
                name (str): A descriptive identifier for the savepoint.
        """
        self.stack.append(_Savepoint(name))

    def rollback(self):
        """
            Reverts the data to the state of the most recent savepoint.

            Pops the last savepoint from the transaction stack and applies its
            recorded deltas. If the stack is empty, the method exits silently.

            The rollback handles two types of restorations:
            1. Full Table: If a '__table__' key exists in the deltas, the entire
               dataframe is restored from that copy.
            2. Column-Level: Iterates through column deltas. If the previous value
               was None, the column is assumed to be new and is dropped. Otherwise,
               the column is restored to its previous values.

            Returns:
                None
        """
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
