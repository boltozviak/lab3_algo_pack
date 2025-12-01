import pytest
from src.structures.stack import Stack
from src.structures.queue import Queue
from src.errors.struct_errors import EmptyStackError, EmptyQueueError


def test_stack_push_pop():
    azaza = Stack()
    azaza.push(10)
    azaza.push(20)
    assert azaza.pop() == 20
    assert azaza.pop() == 10

def test_stack_peek():
    azaza = Stack()
    azaza.push(10)
    azaza.push(20)
    assert azaza.peek() == 20

def test_stack_min():
    azaza = Stack()
    azaza.push(250)
    azaza.push(230)
    azaza.push(70)
    assert azaza.min() == 70

def test_stack_empty_pop():
    azaza = Stack()
    with pytest.raises(EmptyStackError):
        azaza.pop()

def test_queue_enqueue_dequeue():
    azaza = Queue()
    azaza.enqueue(10)
    azaza.enqueue(20)
    assert azaza.dequeue() == 10
    assert azaza.dequeue() == 20

def test_queue_front():
    azaza = Queue()
    azaza.enqueue(10)
    azaza.enqueue(20)
    assert azaza.front() == 10

def test_queue_empty_dequeue():
    azaza = Queue()
    with pytest.raises(EmptyQueueError):
        azaza.dequeue()

def test_queue_empty_front():
    azaza = Queue()
    with pytest.raises(EmptyQueueError):
        azaza.front()
