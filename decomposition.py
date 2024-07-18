import sympy as sp
from sympy.abc import x, y


class Decomposition():

    def __init__(self, data):
        self.data = data

    def get_MRS(self):
        return sp.diff(
            self.data.utility, x
            ) / sp.diff(
                self.data.utility, y
                )

    def equilibration(self):
        pass
