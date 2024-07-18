import sympy as sp


class Numerics():

    def get_budget(self):
        self.budget = int(input(
            'Enter budget: ')
            )

    def get_new_budget(self):
        self.new_budget = int(input(
            'Enter new budget: ')
            )

    def get_prices(self):
        self.prices = (
            int(price) for price in input(
                'Enter prices w/o commas: '
                ).split()
            )

    def get_new_prices(self):
        self.new_prices = (
            int(price) for price in input(
                'Enter new prices w/o commas: '
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
