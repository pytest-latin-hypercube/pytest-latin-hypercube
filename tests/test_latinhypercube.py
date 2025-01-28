import pytest
import m4r

@pytest.mark.parametrize("x", {"x": [0, 1, 2]}, {"x": [0, 1, 2], "y": [0, 1, 2]})
def test_latinhypercube(x):
    M = len(x)
    N = len(next(iter(x.values()), None))
    keys, values = m4r.LatinHypercube(x)
    assert len(keys) == M
    assert len(values) == N
    assert len(values[0]) == M