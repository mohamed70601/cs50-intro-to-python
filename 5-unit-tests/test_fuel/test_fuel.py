import fuel
import pytest


def test_covert():
    assert fuel.convert("1/4") == 25
    assert fuel.convert("1/2") == 50
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/100") == 1
    assert fuel.convert("99/100") == 99
    assert fuel.convert("1/3") == 33
    with pytest.raises(ValueError):
        fuel.convert("5/4")
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")


def test_percentage():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(98) == "98%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
