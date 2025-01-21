import pytest
import numpy as np

def LHparameterised():
    def wrapper():
        LH()
    return wrapper


def LatinHypercube(args: dict, seed: int = 847, K: int = 1):
    """Given a parameter space of N parameters each taking M values, return a Latin Hypercube sample."""
    np.random.seed = seed
    keys = []
    M = len(args)
    N = len(list(args.values())[0])
    samples = [[None for i in range(M)] for j in range(N)]

    for i, (key, value) in enumerate(args.items()):
        keys.append(key)
        if len(value) != N:
            raise ValueError("All parameters' spaces are required to be the same length")

        shuffled_intervals = np.random.permutation(value)
        for j, val in enumerate(shuffled_intervals):
            samples[j][i] = val

    return keys, samples
