from decomposition import Decomposition
from numerics import Numerics


def main():
    input_data = Numerics()
    input_data.get_budget()
    input_data.get_prices()
    input_data.get_new_prices()
    input_data.get_quantities()
    input_data.get_utility_function()
    decomposer = Decomposition(input_data)


if __name__ == '__main__':
    main()
