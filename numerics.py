import sympy as sp


class Numerics:

    def get_budget(self) -> None:
        self.budget = int(input(
            'Enter budget: ')
            )

    def get_prices(self) -> None:
        self.prices = [
            float(price) for price in input(
                'Enter prices w/o commas: '
                ).split()
            ]

    def get_new_prices(self) -> None:
        self.new_prices = [
            float(price) for price in input(
                'Enter new prices w/o commas: '
                ).split()
            ]

    def get_utility_function(self) -> None:
        str_expr = input(
            'Enter utility expression with "x" and "y": '
            )
        self.utility_function = sp.sympify(str_expr)
