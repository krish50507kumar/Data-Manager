class _Savepoint:
    def __init__(self,name):
        self.name = name
        self.deltas = {}
