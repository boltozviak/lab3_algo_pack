from src.errors.sort_errors import InvalidBucketsNumError
from typing import TypeVar


T = TypeVar("T", int, float)

def bucket_sort(arr: list[T], buckets: int | None = None) -> list[T]:
    if buckets is not None and buckets <= 0:
        raise InvalidBucketsNumError(f"Invalid nums of buckets {buckets}")
    if len(arr) <= 1:
        return arr

    max_el, min_el = max(arr), min(arr)
    return recursive_bucket(arr, min_el, max_el, buckets)

def recursive_bucket(arr: list[T], min_el: float, max_el: float, buckets: int | None = None) -> list[T]:

    if len(arr) < 2 or min_el == max_el:
        return arr

    diff = max_el - min_el

    if buckets is None:
        num_buckets = min(len(arr), 250)
    else:
        num_buckets = buckets

    buckets_arr: list[list[T]] = [[] for _ in range(num_buckets)]
    min_buckets = [float("inf")] * num_buckets
    max_buckets = [float("-inf")] * num_buckets

    for num in arr:
        normalized_num = (num - min_el) / diff
        index = int(normalized_num * (num_buckets - 1))
        buckets_arr[index].append(num)
        min_buckets[index] = min(min_buckets[index], num)
        max_buckets[index] = max(max_buckets[index], num)

    for i in range(num_buckets):
        if buckets is None:
            new_buckets = min(len(buckets_arr[i]), 250)
        else:
            new_buckets = buckets
        buckets_arr[i] = recursive_bucket(buckets_arr[i], min_buckets[i], max_buckets[i], new_buckets)

    return [num for bucket in buckets_arr for num in bucket]
