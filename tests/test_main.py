from main import OPERATIONS


def test_operations_maps_symbols_to_functions():
    assert OPERATIONS["+"](2, 3) == 5
    assert OPERATIONS["-"](5, 3) == 2
    assert OPERATIONS["*"](4, 3) == 12
    assert OPERATIONS["/"](10, 2) == 5.0
