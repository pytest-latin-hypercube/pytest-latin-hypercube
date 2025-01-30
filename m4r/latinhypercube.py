import pytest
import numpy as np

def LHparameterised(args: dict, seed: int = 847):
    def wrapper(test_func):
        argnames, argvalues = latin_hypercube(args, seed=seed)
        return pytest.mark.parametrize(argnames, argvalues)(test_func)
    return wrapper


def latin_hypercube(args: dict, seed: int = 847, number_of_iterations: int = 1):
    """Given a parameter space of number_of_arguments parameters each taking N values, return a Latin Hypercube sample."""

    keys = []
    np.random.seed(seed)

    for i, (key, value) in enumerate(args.items()):
        if i == 0:
            longest_parameter_space = len(value)
            perms = []
        keys.append(key)
        if len(value) != longest_parameter_space:
            raise ValueError("All parameters' spaces are required to be the same length")
        perm = np.random.permutation(value*number_of_iterations)
        perms.append(perm)

    return keys, list(zip(*perms))


def latin_hyperrectangle(args: dict, seed: int = 847, number_of_iterations: int = 1):
    """Given a parameter space of longest_parameter_space parameters each taking number_of_arguments values, return a Latin Hypercube sample."""
    keys = []
    longest_parameter_space = 0
    np.random.seed(seed) # change this to something non-global
    for key, value in args.items():
        keys.append(key)
        if len(value) > longest_parameter_space:
            longest_parameter_space = len(value)

    perms = []

    for key, value in args.items():
        if len(value) < longest_parameter_space:
            perm = []
            curr_length = len(value)
            while curr_length < longest_parameter_space*number_of_iterations:
                perm.extend(np.random.permutation(value))
                curr_length = len(perm)
            perm = perm[:longest_parameter_space*number_of_iterations]
        else:
            perm = np.random.permutation(value*number_of_iterations)
        perms.append(perm)

    return keys, list(zip(*perms))
