import pytest
import m4r.latinhypercube

@pytest.mark.parametrize("x", [{"x": [0, 1, 2]}, {"x": [0, 1, 2], "y": [0, 1, 2]}, {"x":[]}, {"x": [0, 1, 2, 4], 2: [0, 1, 2, 3], "z": [0, 2, 5, 1]}])
def test_latinhypercube_length(x):
    M = len(x)
    N = len(next(iter(x.values()), []))
    keys, values = m4r.latinhypercube.LatinHypercube(x)
    assert len(keys) == M
    assert len(values) == N
    if len(values) > 0:
        assert len(values[0]) == M

@pytest.mark.parametrize("seed", [847, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_latinhypercube_seed(seed):
    x = {"x": [0, 1, 2], "y": [0, 1, 2], "z": [0, 1, 2]}
    keys, values = m4r.latinhypercube.LatinHypercube(x, seed=seed)
    keys2, values2 = m4r.latinhypercube.LatinHypercube(x, seed=seed)
    assert keys == keys2
    assert values == values2

@pytest.mark.parametrize("x", [{"x": [0, 1, 2]}, {"x": [0, 1], "y": [0, 1, 2]}, {"x":[]}, {"x": [0, 1, 2, 4], 2: [0, 1, 2, 3], "z": [0, 2, 5, 1]}, {"x": [0, 1, 2, 4], 2: [0, 1], "z": [0, 2, 5]}])
def test_latinhyperrectangle_lengths(x):
    M = len(x)
    N = len(next(iter(x.values()), []))
    for key, value in x.items():
        if len(value) > N:
            N = len(value)
    keys, values = m4r.latinhypercube.LatinHyperRectangle(x)
    assert len(keys) == M
    assert len(values) == N
    if len(values) > 0:
        assert len(values[0]) == M

@pytest.mark.parametrize("seed", [847 + i for i in range(10)])
def test_latinhyperrectangle_seed(seed):
    x = {"x": [0, 1], "y": [0, 1, 2], "z": [0, 1, 2]}
    keys, values = m4r.latinhypercube.LatinHyperRectangle(x, seed=seed)
    keys2, values2 = m4r.latinhypercube.LatinHyperRectangle(x, seed=seed)
    assert keys == keys2
    assert values == values2



@m4r.latinhypercube.LHparameterised({"x": [0, 1, 2], "y": [0, 1, 2], "z": [0, 1, 2]}, seed=847)
def test_latinhypercube_parameterised(x, y, z):
    print(x, y, z)
    assert x in [0, 1, 2]
    assert y in [0, 1, 2]