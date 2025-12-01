from src.errors.func_errors import InvalidValueError


def fibo_iter(n: int) -> int:
    if not isinstance(n, int) or (n < 0):
        raise InvalidValueError("Invalid value")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    first = 0
    second = 1
    for i in range(2, n + 1):
        first, second = second, first + second
    return second

def fibo_recursive(n: int) -> int:
    if not isinstance(n, int) or (n < 0):
        raise InvalidValueError("Invalid value")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)
