import pytest
import numpy as np
import warnings


def LHparameterised(args: dict, seed: int = 847):
    def wrapper(test_func):
        argnames, argvalues = latin_hypercube(args, seed=seed)
        return pytest.mark.parametrize(argnames, argvalues)(test_func)
    return wrapper


def latin_hypercube(args: dict, seed: int = 847,
                    number_of_iterations: int = 1):
    """Given a parameter space of number_of_arguments parameters each taking N
     values, return a Latin Hypercube sample."""

    keys = []
    rng = np.random.default_rng(seed)

    for i, (key, value) in enumerate(args.items()):
        if i == 0:
            longest_parameter_space = len(value)
            perms = []
        keys.append(key)
        if len(value) != longest_parameter_space:
            raise ValueError(
                "All parameters' spaces are required to be the same length")
        perm = rng.permutation(value * number_of_iterations)
        perms.append(perm)

    return keys, list(zip(*perms))


def latin_hyperrectangle(args: dict,
                         seed: int = 847,
                         number_of_iterations: int = 1,
                         max_iteration_factor: int = 10):
    """Given a parameter space of longest_parameter_space parameters each
    taking number_of_arguments values, return a Latin Hypercube sample."""
    keys = []
    longest_parameter_space = 0
    rng = np.random.default_rng(seed)
    for key, value in args.items():
        keys.append(key)
        if len(value) > longest_parameter_space:
            longest_parameter_space = len(value)
    samples = []
    shuffled_args = {key: list(rng.permutation(value * number_of_iterations))
                     for key, value in args.items()}
    iter = 0
    while len(samples) < longest_parameter_space * number_of_iterations:
        iter += 1
        sample = ([shuffled_args[key].pop() for key in keys])
        if sample not in samples:
            samples.append(sample)
        for key, value in args.items():
            if len(shuffled_args[key]) == 0:
                shuffled_args[key] = list(
                    rng.permutation(value * number_of_iterations))

        if iter > (max_iteration_factor * longest_parameter_space * number_of_iterations):
            warnings.warn(
                f"Maximum number of iterations ({(max_iteration_factor * longest_parameter_space * number_of_iterations)}) reached."
                "Returning partial sample.")
            break
    return keys, samples
