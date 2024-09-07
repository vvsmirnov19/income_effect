"""Contains a sequence of actions for calculating effects."""
from decomposition import Decomposition
from numerics import Numerics


def main():
    """Includes main program logic.

    Returns values of effects for both models.
    """
    input_data = Numerics()
    input_data.get_budget()
    input_data.get_prices()
    input_data.get_new_prices()
    input_data.get_utility_function()
    decomposer = Decomposition(input_data)
    decomposer.set_first_equilibration()
    decomposer.set_final_equilibration()
    print('Income effects for x, y via Hicks')
    print(decomposer.income_effect_hicks())
    print('substitution effects for x, y via Hicks')
    print(decomposer.substitution_effect_hicks())
    print('total effects for x, y via Hicks')
    print(decomposer.total_effect(
        decomposer.income_effect_hicks(),
        decomposer.substitution_effect_hicks()
        ))
    print('Income effects for x, y via Slutsky')
    print(decomposer.income_effect_slutsky())
    print('substitution effects for x, y via Slutsky')
    print(decomposer.substitution_effect_slutsky())
    print('total effects for x, y via Slutsky')
    print(decomposer.total_effect(
        decomposer.income_effect_slutsky(),
        decomposer.substitution_effect_slutsky()
        ))


if __name__ == '__main__':
    main()
