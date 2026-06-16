class Runner:
    def __init__(self):
        pass
    def run(self, works = []) :
        if not works:
            return
        try:
            for work in works:
                work["job"].run(work["contexts"])
        except Exception as e:
            raise e
