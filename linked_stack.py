
from node import Node


class LinkedStack:
    """
    Implementasi Stack menggunakan Linked List.
    Prinsip kerja Stack adalah LIFO
    (Last In, First Out).
    """

    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None

        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty():
            return None

        return self.top.data

    def size(self):
        return self._size

    def clear(self):
        self.top = None
        self._size = 0
