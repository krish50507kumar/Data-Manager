from abc import ABC, abstractmethod
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("DataManager")
class BaseJob(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def run(self,context):
        pass

    def savepoint(self,name):
        """
            Creates a new savepoint and pushes it onto the transaction stack.

            This method allows you to mark a specific state in the data's history
            so that it can be reverted to later using the `rollback` method.

            Args:
                name (str): A descriptive identifier for the savepoint.
        """
        logger.info(f"Savepoint: {name}")
        self.storage.savepoint(name)
    def rollback(self):
        logger.info(f"Rollback to : {self.storage.stack[-1] if self.storage.stack else "No savepoint exists"}")
        self.storage.rollback()