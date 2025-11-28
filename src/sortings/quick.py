LENGTH_FOR_INSERTION_SORT = 20

def median_of_three(arr, begin, mid, end):
    a = arr[begin]
    b = arr[mid]
    c = arr[end]
    if ((a > b) ^ (a > c)):
        return begin
    elif ((b < a) ^ (b < c)):
        return mid
    else:
        return end

def insertion_sort(arr: list[int], left: int, right: int):
    '''
    Для оптимизации quick_sort на маленьких массивах
    '''
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def separate_array(arr, left, right):
    pivot_index = median_of_three(arr, left, (left + right) // 2, right)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[(left + right) // 2] = arr[(left + right) // 2], arr[pivot_index]
    i = left
    j = right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def quick_sort_body(arr, left, right):
    if left >= right:
        return

    if right - left + 1 <= LENGTH_FOR_INSERTION_SORT:
        insertion_sort(arr, left, right)
        return

    q = separate_array(arr, left, right)
    quick_sort_body(arr, left, q)
    quick_sort_body(arr, q + 1, right)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    quick_sort_body(arr, 0, len(arr) - 1)
    return arr
