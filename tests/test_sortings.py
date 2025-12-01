import pytest
from src.sortings.bubble import bubble_sort
from src.sortings.quick import quick_sort
from src.sortings.radix import radix_sort
from src.sortings.counting import counting_sort
from src.sortings.heap import heap_sort
from src.sortings.bucket import bucket_sort
from src.errors.sort_errors import TypeSortingError, InvalidBaseError, InvalidBucketsNumError


class TestBubbleSort:
    def test_empty_array(self):
        assert bubble_sort([]) == []

    def test_single_element(self):
        assert bubble_sort([1]) == [1]

    def test_sorted_array(self):
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_array(self):
        assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


class TestQuickSort:
    def test_empty_array(self):
        assert quick_sort([]) == []

    def test_single_element(self):
        assert quick_sort([1]) == [1]

    def test_sorted_array(self):
        assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_array(self):
        assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


class TestHeapSort:
    def test_empty_array(self):
        assert heap_sort([]) == []

    def test_single_element(self):
        assert heap_sort([1]) == [1]

    def test_sorted_array(self):
        assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_array(self):
        assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


class TestCountingSort:
    def test_empty_array(self):
        assert counting_sort([]) == []

    def test_single_element(self):
        assert counting_sort([1]) == [1]

    def test_sorted_array(self):
        assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_array(self):
        assert counting_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_negative_numbers(self):
        assert counting_sort([-5, -1, 0, 3, -2]) == [-5, -2, -1, 0, 3]

    def test_invalid_type_raises_error(self):
        with pytest.raises(TypeSortingError):
            counting_sort([1.5, 2.5, 3.5])  # type: ignore


class TestRadixSort:
    def test_empty_array(self):
        assert radix_sort([]) == []

    def test_single_element(self):
        assert radix_sort([1]) == [1]

    def test_sorted_array(self):
        assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_array(self):
        assert radix_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_large_numbers(self):
        assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]

    def test_negative_numbers(self):
        assert radix_sort([-5, -1, 0, 3, -2]) == [-5, -2, -1, 0, 3]

    def test_invalid_base_raises_error(self):
        with pytest.raises(InvalidBaseError):
            radix_sort([1, 2, 3], base=1)

    def test_custom_base(self):
        assert radix_sort([3, 1, 4, 1, 5, 9, 2, 6], base=2) == [1, 1, 2, 3, 4, 5, 6, 9]


class TestBucketSort:
    def test_empty_array(self):
        assert bucket_sort([]) == []

    def test_single_element(self):
        assert bucket_sort([1]) == [1]

    def test_sorted_array(self):
        assert bucket_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        assert bucket_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_array(self):
        assert bucket_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_float_array(self):
        assert bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]) == [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]

    def test_custom_buckets(self):
        assert bucket_sort([3, 1, 4, 1, 5, 9, 2, 6], buckets=3) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_invalid_buckets_raises_error(self):
        with pytest.raises(InvalidBucketsNumError):
            bucket_sort([1, 2, 3], buckets=0)

    def test_negative_buckets_raises_error(self):
        with pytest.raises(InvalidBucketsNumError):
            bucket_sort([1, 2, 3], buckets=-5)
