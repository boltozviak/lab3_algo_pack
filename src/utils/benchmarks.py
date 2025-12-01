from time import process_time
from typing import Callable


def timeit_once(func, *args, **kwargs) -> float:

    begin = process_time()
    func(*args, **kwargs)
    finish = process_time()
    return (finish - begin) * 1000

def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    ans: dict[str, dict[str, float]] = {}
    for sort_type, func in algos.items():
        ans[sort_type] = {}
        for list_type, arr in arrays.items():
            arr_copy = arr.copy()
            ans[sort_type][list_type] = timeit_once(func,arr_copy)

    return ans
