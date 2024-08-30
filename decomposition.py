import sympy as sp
from sympy.abc import x, y


class Decomposition:

    def __init__(self, data):
        self.data = data

    def get_utility(self, goods):
        return self.data.utility_function.subs({x: goods[0], y: goods[1]})

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
        return sp.solve([max_util_expr, budget_limit])

    def virtual_eq_Hicks(self):
        old_eq = self.equilibration(self.data.prices, self.data.budget)
        old_utility = self.get_utility(old_eq)
        old_utility_eq = sp.Eq(self.data.utility_function, old_utility)
        max_util_expr = self.get_MRS_eq(self.data.new_prices)
        virtual_budget = [
            eq_point * new_price for eq_point, new_price
            in zip(sp.solve(
                [old_utility_eq, max_util_expr]
            ), self.data.new_prices)
        ]
        return self.equilibration(self.data.new_prices, virtual_budget)

    def virtual_eq_Slutsky(self):
        old_eq = self.equilibration(self.data.prices, self.data.budget)
        virtual_budget = [
            eq_point * new_price for eq_point, new_price
            in zip(old_eq, self.data.new_prices)
        ]
        return self.equilibration(self.data.new_prices, virtual_budget)
