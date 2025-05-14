import bank


def test_value():
    assert bank.value("hello") == 0
    assert bank.value("HELLO") == 0
    assert bank.value("hello, world") == 0
    assert bank.value("hi") == 20
    assert bank.value("howdy") == 20
    assert bank.value("goodbye") == 100
    assert bank.value("") == 100
