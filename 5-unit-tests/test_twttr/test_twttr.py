import twttr
import pytest


def test_shorten():
    assert twttr.shorten("cat") == "ct"
    assert twttr.shorten("CAT") == "CT"
    assert twttr.shorten("cat7") == "ct7"
    assert twttr.shorten("cat,") == "ct,"
    with pytest.raises(TypeError):
        twttr.shorten(1)
