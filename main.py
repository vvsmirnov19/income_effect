from decomposition import Decomposition
from numerics import Numerics


def main():
    input_data = Numerics()
    input_data.get_budget()
    input_data.get_prices()
    input_data.get_new_prices()
    input_data.get_utility_function()
    decomposer = Decomposition(input_data)
    decomposer.set_first_equilibration()
    decomposer.set_final_equilibration()
    print('Income effects for x, y via Hicks')
    print(decomposer.income_effect_Hicks())
    print('substitution effects for x, y via Hicks')
    print(decomposer.substitution_effect_Hicks())
    print('total effects for x, y via Hicks')
    print(decomposer.total_effect(
        decomposer.income_effect_Hicks(),
        decomposer.substitution_effect_Hicks()
        ))
    print('Income effects for x, y via Slutsky')
    print(decomposer.income_effect_Slutsky())
    print('substitution effects for x, y via Slutsky')
    print(decomposer.substitution_effect_Slutsky())
    print('total effects for x, y via Slutsky')
    print(decomposer.total_effect(
        decomposer.income_effect_Slutsky(),
        decomposer.substitution_effect_Slutsky()
        ))


if __name__ == '__main__':
    main()
