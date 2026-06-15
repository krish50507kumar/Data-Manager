class _Record:
    def __init__(self,storage):
        self.storage = storage
    def _record_column(self,col):
        if not self.storage.stack :
            return
        sp = self.storage.stack[-1]
        if col not in sp.deltas and '__table__' not in sp.deltas :
            sp.deltas[col] = self.storage.data[col].copy() if col in self.storage.data.columns else None

    def _record_table(self):
        if not self.storage.stack :
            return
        sp = self.storage.stack[-1]
        if '__table__' not in sp.deltas :
            if sp.deltas :
                original = self.storage.data.copy()
                for col,old_vals in sp.deltas.items() :
                    if old_vals is None:
                        original.drop(columns=[col],inplace=True)
                    else:
                        original[col] = old_vals
                sp.deltas = {'__table__':original}
            else:
                sp.deltas['__table__'] = self.storage.data.copy()