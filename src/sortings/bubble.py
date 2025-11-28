from src.errors.sort_errors import TypeSortingError


def bubble_sort(arr: list[int]) -> list[int]:
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise TypeSortingError("Invalid type for sorting") # как лучше валидировать данные в структурах?
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
