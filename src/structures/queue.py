from src.structures.node import Node
from src.errors.struct_errors import EmptyQueueError
from typing import Generic, TypeVar


T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self):
        self.head: Node[T] | None = None
        self.size = 0
        self.tail: Node[T] | None = None

    def enqueue(self, value: T):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self) -> T:
        if self.head is None:
            raise EmptyQueueError("Queue is empty")

        popped_node = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        popped_node.next = None
        self.size -= 1
        return popped_node.value

    def front(self) -> T:
        if self.head is None:
            raise EmptyQueueError("Stack is empty")
        else:
            return self.head.value

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
