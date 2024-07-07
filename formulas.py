import sympy as sp


def budget_constraint_q(price_1, price_2, budget):
    q_1 = budget / price_1
    q_2 = budget / price_2
    return q_1, q_2


def budget_constraint(price_1, price_2, q_1, q_2):
    budget = price_1 * q_1 + price_2 * q_2
    return budget


def utility(v1_param, v1_grade, v2_param, v2_grade):
    mu1 = (m_utility(v1_param, v1_grade), v2_param, v2_grade)
    mu2 = (v1_param, v1_grade, m_utility(v2_param, v2_grade))
    return mu1, mu2


def m_utility(util, x):
    return sp.diff(util, x)
