from pandas import read_excel

class excel(object):
    def __init__(self, io, sheet_name):
        self._data = read_excel(io, sheet_name)

    def __call__(self):
        return data


