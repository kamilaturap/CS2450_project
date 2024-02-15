from mackay import *


def test_load():
    register = {1: '9000'}
    accumulator = load(1, register)
    assert accumulator == '9000'
    print("test_load success")
    return


def test_load_index_error():
    register = {1: '9000'}
    accumulator = load(2, register)
    assert accumulator != '9000'
    print("test_load_index_error success")
    return


def test_store():
    register = {1: "0040"}
    accumulator = '9000'
    store(1, register, accumulator)
    assert register[1] == '9000'
    print("test_store success")
    return


def test_store_index_error():
    register = {1: "0040"}
    accumulator = '9000'
    store(2, register, accumulator)
    assert register[1] != '9000'
    print("test_store_index_error success")
    return


def test_branch():
    register = {1: "0000", 2: "0000", 3: "0000"}
    i = branch(1, register)
    assert i == 0
    print("test_branch success")
    return


def test_branch_index_error():
    register = {1: "0000", 2: "0000", 3: "0000"}
    i = branch(5, register)
    assert i != 4
    print("test_branch_index_error success")
    return


test_load()
test_load_index_error()
test_store()
test_store_index_error()
test_branch()
test_branch_index_error()
