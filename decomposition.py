import sympy as sp
from sympy.abc import x, y

from numerics import Numerics


class Decomposition:

    def __init__(self, data: Numerics):
        self.data = data

    def get_utility(self, goods):
        return self.data.utility_function.subs(goods)

    def get_MRS_eq(self, prices):
        return sp.Eq(sp.diff(
            self.data.utility_function, x
            ) / sp.diff(
                self.data.utility_function, y
                ), prices[0]/prices[1])

    def get_budget_limit(self, prices, budget):
        return sp.Eq(x*prices[0] + y*prices[1], budget)

    def equilibration(self, prices, budget):
        max_util_expr = self.get_MRS_eq(prices)
        budget_limit = self.get_budget_limit(prices, budget)
        answer = sp.solve([max_util_expr, budget_limit])
        if isinstance(answer, list):
            return sp.solve([max_util_expr, budget_limit])[-1]
        return sp.solve([max_util_expr, budget_limit])

    def set_first_equilibration(self):
        self.first_equilibration = self.equilibration(
            self.data.prices, self.data.budget
        )

    def set_final_equilibration(self):
        self.final_equilibration = self.equilibration(
            self.data.new_prices, self.data.budget
        )

    def virtual_eq_Hicks(self):
        old_utility = self.get_utility(self.first_equilibration)
        old_utility_eq = sp.Eq(self.data.utility_function, old_utility)
        max_util_expr = self.get_MRS_eq(self.data.new_prices)
        answer = sp.solve([old_utility_eq, max_util_expr])
        if isinstance(answer, list):
            return sp.solve([old_utility_eq, max_util_expr])[-1]
        return sp.solve([old_utility_eq, max_util_expr])

    def virtual_eq_Slutsky(self):
        virtual_budget = sum([
            eq_point * new_price for eq_point, new_price
            in zip(self.first_equilibration.values(), self.data.new_prices)
        ])
        return self.equilibration(self.data.new_prices, virtual_budget)

    def effect_count(self, first_eq, second_eq):
        return [
            first_x - second_x for first_x, second_x in zip(
                list(first_eq.values()), list(second_eq.values())
            )
        ]

    def income_effect_Hicks(self):
        return self.effect_count(
            self.final_equilibration,
            self.virtual_eq_Hicks()
        )

    def substitution_effect_Hicks(self):
        return self.effect_count(
            self.virtual_eq_Hicks(),
            self.first_equilibration
        )

    def income_effect_Slutsky(self):
        return self.effect_count(
            self.final_equilibration,
            self.virtual_eq_Slutsky()
        )

    def substitution_effect_Slutsky(self):
        return self.effect_count(
            self.virtual_eq_Slutsky(),
            self.first_equilibration
        )

    def total_effect(self, income, substitution):
        return [income_x + substitution_x for
                income_x, substitution_x in zip(income, substitution)]
