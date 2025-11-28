# from src.errors.sort_errors import TypeSortingError

def count_for_radix(arr, pos, base = 10):
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

def radix_sort(arr, base = 10):
    max_num = max(abs(x) for x in arr)
    pos = 1

    positive = [x for x in arr if x >= 0]
    negative = [-x for x in arr if x < 0]

    while max_num // pos != 0:
        positive = count_for_radix(positive, pos, base)
        negative = count_for_radix(negative, pos, base)
        pos *= base

    negative.reverse()
    res = [x * -1 for x in negative] + positive
    return res


# def radix_sort_with_buckets(arr):
#     '''
#     Без внешней стабильной сортировки + не работает с отрицательными
#     '''
#     if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
#         raise TypeSortingError("Invalid type for sorting") # как лучше валидировать данные в структурах?

#     max_num = max(arr)
#     pos = 1
#     positive = [x for x in arr if x >= 0]
#     negative = [x for x in arr if x < 0]

#     while max_num // pos > 0:
#         buckets_pos = [[] for _ in range(10)]
#         buckets_neg = [[] for _ in range(10)]

#         for num in arr:
#             index = (num // pos) % 10
#             buckets[index].append(num)

#         arr = [num for bucket in buckets for num in bucket]
#         pos *= 10

#     return arr
