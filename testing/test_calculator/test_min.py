from calculator.minimum import minimum


def test_min():
    assert minimum(5, 7) == 5
    assert minimum(4, 4) == 4