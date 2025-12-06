from numpy import random
from src.errors.func_errors import NotEnoughUniqueValues


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    if distinct:
        if hi - lo < n:
            raise NotEnoughUniqueValues("Small range for unique numbers")
        arr = random.choice(range(lo, hi), size=n, replace=False)
    else:
        arr = random.randint(lo, hi, size=n)

    return arr.tolist()


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    arr = list(range(n))

    for _ in range(swaps):
        first, second = random.randint(0, n, size = 2)
        arr[first], arr[second] = arr[second], arr[first]

    return arr

def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    res = random.choice(range(k_unique), size=n)
    return res.tolist()


def reverse_sorted(n: int) -> list[int]:
    arr = list(range(n-1, -1, -1))
    return arr


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    if seed is not None:
        random.seed(seed)

    arr = random.uniform(lo, hi, size=n)
    return arr.tolist()
