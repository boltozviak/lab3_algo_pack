from typing import TypeVar


T = TypeVar("T", int, float, str)

def heapify(arr: list[T], n: int, root: int):
    max_el = root
    left = 2 * root + 1
    right = 2 * root + 2
    if left < n and arr[left] > arr[max_el]:
        max_el = left

    if right < n and arr[right] > arr[max_el]:
        max_el = right

    if max_el != root:
        arr[root], arr[max_el] = arr[max_el], arr[root]
        heapify(arr, n, max_el)


def heap_sort(arr: list[T]) -> list[T]:
    if len(arr) <= 1:
        return arr
    arr_len = len(arr)
    for i in range(arr_len // 2 - 1, -1, -1):
        heapify(arr, arr_len, i)

    for i in range(arr_len - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
