from main import *

def test_read(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1234")
    memory = '05'
    dic = {0:'', 1:'', 2:'', 3:'', 4:'', 5:''}
    read(memory, dic)
    assert dic[5] == '1234'

def test_read_new_register(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1234")
    memory = '06'
    dic = {0:'', 1:'', 2:'', 3:'', 4:'', 5:''}
    read(memory, dic)
    assert dic[6] == '1234'

def test_write(capsys):
    memory = '05'
    dic = {0:'', 1:'', 2:'', 3:'', 4:'', 5:'1234'}
    write(memory, dic)
    captured = capsys.readouterr()
    assert captured.out == '1234\n'


def test_write_empty_register(capsys):
    memory = '04'
    dic = {0:'', 1:'', 2:'', 3:'', 4:'', 5:'1234'}
    write(memory, dic)
    captured = capsys.readouterr()
    assert captured.out == '\n'
