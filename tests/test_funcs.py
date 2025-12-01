import pytest
from src.funcs.fact import fact_iter, fact_recursive
from src.funcs.fibo import fibo_iter, fibo_recursive
from src.errors.func_errors import InvalidValueError



def test_fact_iter():
    assert fact_iter(6) == 720

def test_fact_recursive():
    assert fact_recursive(6) == 720

def test_fact_iter_negative():
    with pytest.raises(InvalidValueError):
        fact_iter(-22)

def test_fact_recursive_negative():
    with pytest.raises(InvalidValueError):
        fact_recursive(-14)

def test_fact_iter_float():
    with pytest.raises(InvalidValueError):
        fact_iter(3.14)

def test_fact_recursive_float():
    with pytest.raises(InvalidValueError):
        fact_recursive(3.14)

def test_fibo_iter():
    assert fibo_iter(8) == 21

def test_fibo_recursive():
    assert fibo_recursive(8) == 21

def test_fibo_iter_negative():
    with pytest.raises(InvalidValueError):
        fibo_iter(-11)

def test_fibo_recursive_negative():
    with pytest.raises(InvalidValueError):
        fibo_recursive(-125)

def test_fibo_iter_float():
    with pytest.raises(InvalidValueError):
        fibo_iter(3.14)

def test_fibo_recursive_float():
    with pytest.raises(InvalidValueError):
        fibo_recursive(3.14)
