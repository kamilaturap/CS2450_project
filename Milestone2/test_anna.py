from anna import *

def test_add():
    register = {1: '1000'}
    accumulator = 100
    accumulator += add(1, register)
    assert accumulator == 1100

def test_add_fail():
    register = {1: '1000'}
    accumulator = 2000
    accumulator += add(1, register)
    
    assert accumulator !=2000

def test_divide():
    register = {1: '1000'}
    accumulator = 2000
    accumulator /= divide(1, register)
    
    assert accumulator == 2

def test_divide_fail():
    register = {1: '500'}
    accumulator = 4000
    accumulator /= divide(1, register)

    assert accumulator != 300

def test_branchneg():
    accumulator = -2
    current_index = 4
    result = branchneg(1, accumulator, current_index)
    return 0

def test_branchnotneg():
    accumulator = 10
    current_index = 6
    result = branchneg(1, accumulator, current_index)
    return 0


test_add()
test_add_fail()
test_divide()
test_divide_fail()
test_branchneg()
test_branchnotneg()