from typing import TypeVar


T = TypeVar("T", int, float, str)


def bubble_sort(arr: list[T]) -> list[T]:
    if len(arr) <= 1:
        return arr
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
