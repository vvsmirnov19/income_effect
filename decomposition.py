"""Includes Decomposition class."""
from typing import Any

import sympy as sp
from sympy.abc import x, y

from numerics import Numerics


class Decomposition:
    """Core class that provides all calculations and results effects."""

    def __init__(self, data: Numerics):
        """Set Numerics into Decomposition field."""
        self.data = data

    def get_utility(self, goods: dict[sp.Wild, Any]) -> float:
        """Calculate utility value."""
        return self.data.utility_function.subs(goods)

    def get_mrs_eq(self, prices: list[int | float]) -> sp.Equality:
        """Return MRS equation."""
        return sp.Eq(sp.diff(
            self.data.utility_function, x
            ) / sp.diff(
                self.data.utility_function, y
                ), prices[0]/prices[1])

    def get_budget_limit(
            self,
            prices: list[int | float],
            budget: int
            ) -> sp.Equality:
        """Calculate budget limit."""
        return sp.Eq(x*prices[0] + y*prices[1], budget)

    def equilibration(
            self,
            prices: list[int | float],
            budget: int
            ) -> dict[sp.Wild, Any]:
        """Calculate values of products for customer's optimal choice."""
        max_util_expr = self.get_mrs_eq(prices)
        budget_limit = self.get_budget_limit(prices, budget)
        answer = sp.solve([max_util_expr, budget_limit])
        if isinstance(answer, list):
            return sp.solve([max_util_expr, budget_limit])[-1]
        return sp.solve([max_util_expr, budget_limit])

    def set_first_equilibration(self) -> None:
        """Set values of products for optimal choice with old prices."""
        self.first_equilibration = self.equilibration(
            self.data.prices, self.data.budget
        )

    def set_final_equilibration(self) -> None:
        """Set values of products for optimal choice with new prices."""
        self.final_equilibration = self.equilibration(
            self.data.new_prices, self.data.budget
        )

    def virtual_eq_hicks(self) -> dict[sp.Wild, Any]:
        """Return optimal choice for helping line in Hicks model."""
        old_utility = self.get_utility(self.first_equilibration)
        old_utility_eq = sp.Eq(self.data.utility_function, old_utility)
        max_util_expr = self.get_mrs_eq(self.data.new_prices)
        answer = sp.solve([old_utility_eq, max_util_expr])
        if isinstance(answer, list):
            return sp.solve([old_utility_eq, max_util_expr])[-1]
        return sp.solve([old_utility_eq, max_util_expr])

    def virtual_eq_slutsky(self) -> dict[sp.Wild, Any]:
        """Return optimal choice for helping line in Slutsky model."""
        virtual_budget = sum([
            eq_point * new_price for eq_point, new_price
            in zip(self.first_equilibration.values(), self.data.new_prices)
        ])
        return self.equilibration(self.data.new_prices, virtual_budget)

    def effect_count(
            self,
            first_eq: dict[sp.Wild, Any],
            second_eq: dict[sp.Wild, Any]
            ) -> list[float]:
        """Count values of particular effect."""
        return [
            first_x - second_x for first_x, second_x in zip(
                list(first_eq.values()), list(second_eq.values())
            )
        ]

    def income_effect_hicks(self) -> list[float]:
        """Count values of income effect for Hicks model."""
        return self.effect_count(
            self.final_equilibration,
            self.virtual_eq_hicks()
        )

    def substitution_effect_hicks(self) -> list[float]:
        """Count values of substitution effect for Hicks model."""
        return self.effect_count(
            self.virtual_eq_hicks(),
            self.first_equilibration
        )

    def income_effect_slutsky(self) -> list[float]:
        """Count values of income effect for Slutsky model."""
        return self.effect_count(
            self.final_equilibration,
            self.virtual_eq_slutsky()
        )

    def substitution_effect_slutsky(self) -> list[float]:
        """Count values of substitution effect for Slutsky model."""
        return self.effect_count(
            self.virtual_eq_slutsky(),
            self.first_equilibration
        )

    def total_effect(self, income, substitution) -> list[float]:
        """Count values of effects for both models."""
        return [income_x + substitution_x for
                income_x, substitution_x in zip(income, substitution)]
