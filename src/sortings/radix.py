# from src.errors.sort_errors import TypeSortingError
from src.errors.sort_errors import InvalidBaseError

def count_for_radix(arr: list[int], pos: int, base: int = 10) -> list[int]:
    pref = [0] * base  # Размер должен соответствовать base

    for num in arr:
        index = (num // pos) % base
        pref[index] += 1

    for num in range(1, len(pref)):
        pref[num] += pref[num - 1]

    res = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        index = (arr[i] // pos) % base
        pref[index] -= 1
        res[pref[index]] = arr[i]

    return res

def radix_sort(arr: list[int], base: int = 10) -> list[int]:
    if base <= 1:
        raise InvalidBaseError(f"Invalid base {base}")
    if len(arr) <= 1:
        return arr
    max_num = max(abs(x) for x in arr)
    pos = 1

    positive = [x for x in arr if x >= 0]
    negative = [x * -1 for x in arr if x < 0]

    while max_num // pos != 0:
        positive = count_for_radix(positive, pos, base)
        negative = count_for_radix(negative, pos, base)
        pos *= base

    negative.reverse()
    res = [x * -1 for x in negative] + positive
    return res
