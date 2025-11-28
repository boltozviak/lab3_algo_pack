from src.errors.sort_errors import TypeSortingError


def counting_sort(arr):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise TypeSortingError("Invalid type for sorting") # как лучше валидировать данные в структурах?

    if len(arr) <= 1:
        return arr

    min_el, max_el = min(arr), max(arr)

    pref = [0] * (max_el - min_el + 1)

    for i in arr:
        pref[i - min_el] += 1

    for i in range(1, len(pref)):
        pref[i] += pref[i - 1]

    res = [0] * len(arr)
    for i in reversed(arr):
        index = i - min_el
        pref[index] -= 1
        res[pref[index]] = i

    return res
