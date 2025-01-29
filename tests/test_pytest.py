import pytest


@pytest.fixture(params=[i for i in range(2)])
def data_set(request):
    print(request)
    return request.param


@pytest.fixture(params=[i for i in range(2)])
def data_set2(request):
    print(request)
    return request.param


@pytest.fixture
def order(data_set, data_set2):
    print(order)
    return [data_set, data_set2]


def test_data(order):
    print(order)
    pass
