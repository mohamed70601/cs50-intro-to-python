import plates


def test_valid_plates():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("HELLO") == True
    assert plates.is_valid("ECTO88") == True


def test_invalid_length():
    assert plates.is_valid("H") == False
    assert plates.is_valid("OUTATIME") == False


def test_first_two_chars():
    assert plates.is_valid("50CS") == False
    assert plates.is_valid("C5") == False
    assert plates.is_valid("5") == False


def test_number_placement():
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("CS50P") == False


def test_special_chars():
    assert plates.is_valid("HEL,LO") == False
    assert plates.is_valid("HELLO!") == False
