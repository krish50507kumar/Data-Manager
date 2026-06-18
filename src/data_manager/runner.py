import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("DataManager")

class Runner:
    def __init__(self,works):
        self.works = works

    def run(self) :
        if not self.works:
            logger.info("No works")
            return
        try:
            logger.info("Starting works")
            for work in self.works:
                logger.info(f"Starting work {work["job"]}")
                work["job"].run(work["contexts"])
        except Exception as e:
            raise e
