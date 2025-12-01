import pytest
from src.funcs.fact import fact_iter, fact_recursive
from src.funcs.fibo import fibo_iter, fibo_recursive
from src.errors.func_errors import InvalidValueError


class TestFactorial:
    def test_fact_iter_zero(self):
        assert fact_iter(0) == 1

    def test_fact_iter_one(self):
        assert fact_iter(1) == 1

    def test_fact_iter_positive(self):
        assert fact_iter(5) == 120
        assert fact_iter(10) == 3628800

    def test_fact_recursive_zero(self):
        assert fact_recursive(0) == 1

    def test_fact_recursive_one(self):
        assert fact_recursive(1) == 1

    def test_fact_recursive_positive(self):
        assert fact_recursive(5) == 120
        assert fact_recursive(10) == 3628800

    def test_fact_iter_negative_raises_error(self):
        with pytest.raises(InvalidValueError):
            fact_iter(-1)

    def test_fact_recursive_negative_raises_error(self):
        with pytest.raises(InvalidValueError):
            fact_recursive(-1)

    def test_fact_iter_invalid_type(self):
        with pytest.raises(InvalidValueError):
            fact_iter(3.14)  # type: ignore

    def test_fact_recursive_invalid_type(self):
        with pytest.raises(InvalidValueError):
            fact_recursive("5")  # type: ignore


class TestFibonacci:
    def test_fibo_iter_zero(self):
        assert fibo_iter(0) == 0

    def test_fibo_iter_one(self):
        assert fibo_iter(1) == 1

    def test_fibo_iter_positive(self):
        assert fibo_iter(5) == 5
        assert fibo_iter(10) == 55
        assert fibo_iter(15) == 610

    def test_fibo_recursive_zero(self):
        assert fibo_recursive(0) == 0

    def test_fibo_recursive_one(self):
        assert fibo_recursive(1) == 1

    def test_fibo_recursive_positive(self):
        assert fibo_recursive(5) == 5
        assert fibo_recursive(10) == 55

    def test_fibo_iter_negative_raises_error(self):
        with pytest.raises(InvalidValueError):
            fibo_iter(-1)

    def test_fibo_recursive_negative_raises_error(self):
        with pytest.raises(InvalidValueError):
            fibo_recursive(-1)

    def test_fibo_iter_invalid_type(self):
        with pytest.raises(InvalidValueError):
            fibo_iter(3.14)  # type: ignore

    def test_fibo_recursive_invalid_type(self):
        with pytest.raises(InvalidValueError):
            fibo_recursive("5")  # type: ignore
