import pytest

from main import binary_search

@pytest.fixture
def even_list():
    return list(range(256))

@pytest.fixture
def odd_list():
    return list(range(99))

def test_empty_list():
    with pytest.raises(ValueError):
        binary_search([], 1)

def test_single_item():
    assert 0 == binary_search([3], 3)

def test(even_list):
    assert 1 == binary_search(even_list, 1)

def test_odd_list(odd_list):
    assert 1 == binary_search(odd_list, 1)


def test_first_element(even_list):
    assert 0 == binary_search(even_list, 0)

def test_last_element(even_list):
    assert 255 == binary_search(even_list, 255)

def test_nonexistent_element(even_list):
    with pytest.raises(ValueError):
        binary_search(even_list, 300)