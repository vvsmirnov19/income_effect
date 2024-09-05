"""Provide class for data input."""
import sympy as sp


class Numerics:
    """Get data for calculation from user's input."""

    def get_budget(self) -> None:
        """Transfers budget into the class field."""
        self.budget = int(input(
            'Enter budget: ')
            )

    def get_prices(self) -> None:
        """Transfers prices into the class field."""
        self.prices = [
            float(price) for price in input(
                'Enter prices w/o commas: '
                ).split()
            ]

    def get_new_prices(self) -> None:
        """Transfers new prices into the class field."""
        self.new_prices = [
            float(price) for price in input(
                'Enter new prices w/o commas: '
                ).split()
            ]

    def get_utility_function(self) -> None:
        """Transfers utility function into the class field."""
        str_expr = input(
            'Enter utility expression with "x" and "y": '
            )
        self.utility_function = sp.sympify(str_expr)
