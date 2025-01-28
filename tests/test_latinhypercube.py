import pytest
import m4r.latinhypercube

@pytest.mark.parametrize("x", [{"x": [0, 1, 2]}, {"x": [0, 1, 2], "y": [0, 1, 2]}, {"x":[]}, {"x": [0, 1, 2, 4], 2: [0, 1, 2, 3], "z": [0, 2, 5, 1]}])
def test_latinhypercube(x):
    M = len(x)
    N = len(next(iter(x.values()), []))
    keys, values = m4r.latinhypercube.LatinHypercube(x)
    assert len(keys) == M
    assert len(values) == N
    if len(values) > 0:
        assert len(values[0]) == M

@m4r.latinhypercube.LHparameterised({"x": [0, 1, 2], "y": [0, 1, 2], "z": [0, 1, 2]}, seed=847)
def test_latinhypercube_parameterised(x, y, z):
    print(x, y, z)
    assert x in [0, 1, 2]
    assert y in [0, 1, 2]