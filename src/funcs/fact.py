from src.errors.func_errors import InvalidValueError


def fact(n: int) -> int:
    if not isinstance(n, int) or (n < 0):
        raise InvalidValueError("Invalid value")
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

def fact_recursive(n: int) -> int:
    if not isinstance(n, int) or (n < 0):
        raise InvalidValueError("Invalid value")
    if n == 0 or n == 1:
        return 1
    return n * fact_recursive(n - 1)
