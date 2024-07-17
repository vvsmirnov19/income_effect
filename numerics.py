import sympy as sp


class numerics():

    def get_budget(self):
        self.budget = int(input(
            'Enter budget: ')
            )

    def get_prices(self):
        self.prices = (
            int(price) for price in input(
                'Enter prices w/o commas: '
                ).split()
            )

    def get_quantities(self):
        self.quantities = (
            int(quantity) for quantity in input(
                'Enter quantities w/o commas: '
                )
        )

    def get_utility(self):
        str_expr = input(
            'Enter untility expression with "x" and "y": '
            )
        self.utility = sp.sympify(str_expr)
