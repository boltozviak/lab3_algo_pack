from src.structures.node import Node
from src.errors.struct_errors import EmptyQueueError, StructureTypeError


class Queue:
    def __init__(self):
        self.type = None # как ещё можно проверять тип
        self.head = None
        self.size = 0
        self.tail = None

    def enqueue(self, value):
        if self.type is None:
            self.type = type(value)
        else:
            if type(value) is not self.type:
                raise StructureTypeError(f"Expected {self.type.__name__}; got {type(value).__name__}")

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        popped_node = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        popped_node.next = None
        self.size -= 1
        return popped_node.value

    def front(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        else:
            return self.head.value

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        nodes = []
        inter_node = self.head
        while inter_node:
            nodes.append(str(inter_node.value))
            inter_node = inter_node.next
        return "Queue(head -> tail): " + " ".join(nodes)
