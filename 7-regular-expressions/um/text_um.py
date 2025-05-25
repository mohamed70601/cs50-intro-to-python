from um import count


def test_count():
    assert count("um") == 1
    assert count("Um, thanks, um...") == 2
    assert count("yummy") == 0
    assert count("Hello, world!") == 0
    assert count("UM UM uM um") == 4
    assert count("um?") == 1
    assert count("um um um, um um, um um um um um um aaam") == 11
