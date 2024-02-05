from kamila import *


def test_subtract():
    register = {1: '1000'}
    accumulator = 2000
    result = subtract(1, register, accumulator)
    assert result == 1000


def test_multiply():
    register = {1: '1000'}
    accumulator = 5
    result = multiply(1, register, accumulator)
    assert result == 5000


def test_branchzero():
    # branch when accumulator is zero
    accumulator_zero = 0
    current_index_zero = 5
    result_zero = branchzero(2, accumulator_zero, current_index_zero)
    assert result_zero == 1

    # don't branch when accumulator is not zero
    accumulator_nonzero = 5
    current_index_nonzero = 7
    result_nonzero = branchzero(1, accumulator_nonzero, current_index_nonzero)
    assert result_nonzero == current_index_nonzero


test_subtract()
test_multiply()
test_branchzero()
