import pytest
import numpy as np

def LHparameterised():
    def wrapper():
        
    return wrapper


def LatinHypercube(args: dict, seed: int = 847, K: int = 1):
    """Given a parameter space of M parameters each taking K values, return a Latin Hypercube sample."""
    np.random.seed = seed
    keys = []
    M = len(args)
    samples = [[None for _ in range(M)] for _ in range(N*K)]

    for k in range(K):
        for i, (key, value) in enumerate(args.items()):
            if i == 0:
                N = len(value)
            keys.append(key)
            if len(value) != N:
                raise ValueError("All parameters' spaces are required to be the same length")

            shuffled_intervals = np.random.permutation(value)
            for j, val in enumerate(shuffled_intervals):
                samples[j][k*N + i] = val

    return keys, samples

def LatinHyperRectangle(args: dict, seed: int = 847, K: int = 1):
    """Given a parameter space of N parameters each taking M values, return a Latin Hypercube sample."""
    np.random.seed = seed
    keys = []
    M = len(args)
    lengths = []

    for i, (key, value) in enumerate(args.items()):
        keys.append(key)
        lengths.append(len(value))
    
    N = max(lengths)
    samples = [[None for _ in range(M)] for _ in range(N)]

    for k in range(K):
        for i, (key, value) in enumerate(args.items()):
            keys.append(key)
            shuffled_intervals = []
            if len(value) < N:
                curr_length = len(value)
                while curr_length < N:
                    shuffled_intervals.extend(np.random.permutation(value))
                    curr_length = len(shuffled_intervals)
                shuffled_intervals = shuffled_intervals[:N]    
            else:
                shuffled_intervals = np.random.permutation(value)

            for j, val in enumerate(shuffled_intervals):
                samples[j][k*N + i] = val

    return keys, samples
