import pytest
from src.sortings.bubble import bubble_sort
from src.sortings.quick import quick_sort
from src.sortings.radix import radix_sort
from src.sortings.counting import counting_sort
from src.sortings.heap import heap_sort
from src.sortings.bucket import bucket_sort
from src.errors.sort_errors import TypeSortingError, InvalidBaseError, InvalidBucketsNumError
from src.utils.test_generator import rand_int_array

arr = rand_int_array(128, 0, 10000, seed=10)
sorted_arr = sorted(arr)

def test_bubble_sort_basic():
    assert bubble_sort(arr) == sorted_arr

def test_quick_sort_basic():
    assert quick_sort(arr) == sorted_arr

def test_radix_sort_basic():
    assert radix_sort(arr) == sorted_arr

def test_radix_sort_negative():
    assert radix_sort(arr) == sorted_arr

def test_radix_sort_invalid_base():
    with pytest.raises(InvalidBaseError):
        radix_sort(arr, base=0)

def test_counting_sort_basic():
    assert counting_sort(arr) == sorted_arr

def test_counting_sort_invalid_type():
    with pytest.raises(TypeSortingError):
        counting_sort([1.5, 2.3])

def test_heap_sort_basic():
    assert heap_sort(arr) == sorted_arr


def test_bucket_sort_basic():
    assert bucket_sort(arr) == sorted_arr


def test_bucket_sort_invalid_buckets():
    with pytest.raises(InvalidBucketsNumError):
        bucket_sort(arr, buckets=0)
