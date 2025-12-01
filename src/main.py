from src.sortings.bubble import bubble_sort
from src.sortings.quick import quick_sort
from src.sortings.heap import heap_sort
from src.sortings.counting import counting_sort
from src.sortings.radix import radix_sort
from src.sortings.bucket import bucket_sort
from src.utils.benchmarks import benchmark_sorts
from src.utils.test_generator import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted


def run_benchmarks():
    '''
    Отчёт с бенчмарками
    '''
    arrays = {
        "rand_int": rand_int_array(10000, 0, 10000, seed=10),
        "nearly_sorted": nearly_sorted(10000, 1000, seed=10),
        "many_duplicates": many_duplicates(10000, 5, seed=10),
        "reverse_sorted": reverse_sorted(10000),
    }

    algos = {
        "bubble": bubble_sort,
        "quick": quick_sort,
        "radix": radix_sort,
        "bucket": bucket_sort,
        "counting": counting_sort,
        "heap": heap_sort,
    }


    results = benchmark_sorts(arrays, algos)
    for k, v in results.items():
        print(f"{k}: \n")
        for k2,v2 in v.items():
            print(f"{k2}: {v2} мс\n")

def main():
    run_benchmarks()

if __name__ == "__main__":
    main()
