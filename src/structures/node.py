from typing import Generic, TypeVar


T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value
        self.next: Node[T] | None = None
        self.min: T | None = None
