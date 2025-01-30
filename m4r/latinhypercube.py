import pytest
import numpy as np

def LHparameterised(args: dict, seed: int = 847):
    def wrapper(test_func):
        argnames, argvalues = latin_hyperrectangle(args, seed=seed)
        return pytest.mark.parametrize(argnames, argvalues)(test_func)
    return wrapper


def latin_hypercube(args: dict, seed: int = 847, number_of_iterations: int = 1):
    """Given a parameter space of number_of_arguments parameters each taking N values, return a Latin Hypercube sample."""

    keys = []
    number_of_arguments = len(args)
    np.random.seed(seed) # 

    for k in range(number_of_iterations):
        for i, (key, value) in enumerate(args.items()):
            if i == 0:
                longest_parameter_space = len(value)
                samples = [[None for _ in range(number_of_arguments)] for _ in range(longest_parameter_space*number_of_iterations)]
            keys.append(key)
            if len(value) != longest_parameter_space:
                raise ValueError("All parameters' spaces are required to be the same length")
            shuffled_intervals = np.random.permutation(value)
            for j, val in enumerate(shuffled_intervals):
                samples[k*longest_parameter_space + i][j]= val

    return keys, samples


def latin_hyperrectangle(args: dict, seed: int = 847, number_of_iterations: int = 1):
    """Given a parameter space of longest_parameter_space parameters each taking number_of_arguments values, return a Latin Hypercube sample."""
    keys = []
    number_of_arguments = len(args) # give variables better names
    lengths = []
    np.random.seed(seed) # change this to something non-global
    for i, (key, value) in enumerate(args.items()):
        keys.append(key)
        lengths.append(len(value))

    longest_parameter_space = max(lengths)
    samples = [[None for _ in range(number_of_arguments)] for _ in range(number_of_iterations*longest_parameter_space)]

    for k in range(number_of_iterations): #use zip and make this make more sense
        for i, (key, value) in enumerate(args.items()):
            if len(value) < longest_parameter_space:
                shuffled_intervals = []
                curr_length = len(value)
                while curr_length < longest_parameter_space:
                    shuffled_intervals.extend(np.random.permutation(value))
                    curr_length = len(shuffled_intervals)
                shuffled_intervals = shuffled_intervals[:longest_parameter_space]
            else:
                shuffled_intervals = np.random.permutation(value)

            for j, val in enumerate(shuffled_intervals):
                samples[k*longest_parameter_space + i][j] = val

    return keys, samples
