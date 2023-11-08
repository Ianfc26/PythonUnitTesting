import mathtest


def test_add():
    expected = 6
    actual = mathtest.add(1, 2, 3)

    assert expected == actual
def test_add_list():
    nums = [2,3,4,5]

    expected = sum(nums)
    actual = mathtest.add(*nums)

    assert expected == actual
def test_mult():
    expected = 16
    actual = mathtest.mult(2, 2, 4)

    assert expected == actual
def test_mult_list():
    nums = [4, 4, 2]

    expected = 32
    actual = mathtest.mult(*nums)

    assert expected == actual