from src.structures.node import Node
from src.errors.struct_errors import EmptyStackError, StructureTypeError


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        self.type = None

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            self.size -= 1
            return popped_node.value

    def push(self, value):
        if self.type is None:
            self.type = type(value)
        else:
            if type(value) is not self.type:
                raise StructureTypeError(f"Type error: expected {self.type.__name__}, got {type(value).__name__}")

        if self.head is None:
            self.head = Node(value)
            self.head.min = value
        else:
            new_node = Node(value)
            new_node.next = self.head
            new_node.min = min(value, self.head.min)
            self.head = new_node
        self.size += 1

    def min(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.head.min

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        else:
            return self.head.value

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        nodes = []
        inter_node = self.head
        while inter_node:
            nodes.append(str(inter_node.value))
            inter_node = inter_node.next
        return "Stack(head -> bottom): " + " -> ".join(nodes)
