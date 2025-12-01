import pytest
from src.structures.stack import Stack
from src.structures.queue import Queue
from src.errors.struct_errors import EmptyStackError, EmptyQueueError


class TestStack:
    """Тесты для структуры данных Stack"""

    def test_stack_init(self):
        stack = Stack[int]()
        assert stack.is_empty()
        assert len(stack) == 0

    def test_stack_push(self):
        stack = Stack[int]()
        stack.push(1)
        assert not stack.is_empty()
        assert len(stack) == 1

    def test_stack_push_multiple(self):
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert len(stack) == 3

    def test_stack_pop(self):
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        value = stack.pop()
        assert value == 2
        assert len(stack) == 1

    def test_stack_pop_order(self):
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_stack_peek(self):
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert len(stack) == 2  # Peek не удаляет элемент

    def test_stack_min(self):
        stack = Stack[int]()
        stack.push(5)
        stack.push(3)
        stack.push(7)
        stack.push(1)
        assert stack.min() == 1
        stack.pop()
        assert stack.min() == 3

    def test_stack_pop_empty_raises_error(self):
        stack = Stack[int]()
        with pytest.raises(EmptyStackError):
            stack.pop()

    def test_stack_peek_empty_raises_error(self):
        stack = Stack[int]()
        with pytest.raises(EmptyStackError):
            stack.peek()

    def test_stack_min_empty_raises_error(self):
        stack = Stack[int]()
        with pytest.raises(EmptyStackError):
            stack.min()


class TestQueue:
    """Тесты для структуры данных Queue"""

    def test_queue_init(self):
        queue = Queue[int]()
        assert queue.is_empty()
        assert len(queue) == 0

    def test_queue_enqueue(self):
        queue = Queue[int]()
        queue.enqueue(1)
        assert not queue.is_empty()
        assert len(queue) == 1

    def test_queue_enqueue_multiple(self):
        queue = Queue[int]()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert len(queue) == 3

    def test_queue_dequeue(self):
        queue = Queue[int]()
        queue.enqueue(1)
        queue.enqueue(2)
        value = queue.dequeue()
        assert value == 1
        assert len(queue) == 1

    def test_queue_dequeue_order(self):
        queue = Queue[int]()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3

    def test_queue_front(self):
        queue = Queue[int]()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.front() == 1
        assert len(queue) == 2  # Front не удаляет элемент

    def test_queue_dequeue_empty_raises_error(self):
        queue = Queue[int]()
        with pytest.raises(EmptyQueueError):
            queue.dequeue()

    def test_queue_front_empty_raises_error(self):
        queue = Queue[int]()
        with pytest.raises(EmptyQueueError):
            queue.front()

    def test_queue_mixed_operations(self):
        queue = Queue[int]()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        queue.enqueue(3)
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.is_empty()
