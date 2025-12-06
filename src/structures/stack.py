from src.structures.node import Node
from src.errors.struct_errors import EmptyStackError
from typing import Generic, TypeVar, Protocol


class SupportsLessThan(Protocol):    # для решения
    def __lt__(self, other) -> bool: # error: No overload variant of "min" matchesargument types "T", "T"
        ...

T = TypeVar("T", bound=SupportsLessThan)

class Stack(Generic[T]):
    def __init__(self):
        self.head: Node[T] | None = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def pop(self) -> T:
        if self.head is None:
            raise EmptyStackError("Stack is empty")
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            self.size -= 1
            return popped_node.value

    def push(self, value: T):
        if self.head is None:
            self.head = Node(value)
            self.head.min = value
        else:
            new_node = Node(value)
            new_node.next = self.head
            if self.head.min is not None:
                new_node.min = min(value, self.head.min)# type: ignore[type-var]
            else:
                new_node.min = value
            self.head = new_node
        self.size += 1

    def min(self) -> T | None:
        if self.head is None:
            raise EmptyStackError("Stack is empty")
        return self.head.min

    def peek(self) -> T:
        if self.head is None:
            raise EmptyStackError("Stack is empty")
        else:
            return self.head.value

    def __len__(self):
        return self.size
