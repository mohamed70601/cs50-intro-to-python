from seasons import minutes_lived
import pytest


def test_minutes_lived():
    assert (
        minutes_lived(2000, 1, 1)
        == "Thirteen million, three hundred sixty-six thousand eighty minutes"
    )
    assert (
        minutes_lived(2019, 1, 1)
        == "Three million, three hundred seventy-two thousand, four hundred eighty minutes"
    )
    with pytest.raises(SystemExit):
        minutes_lived("2024", "02", "30")
