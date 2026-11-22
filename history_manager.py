
from linked_stack import LinkedStack


class HistoryManager:
    """
    Mengelola riwayat Undo dan Redo
    menggunakan dua Linked Stack.
    """

    def __init__(self):
        self.undo_stack = LinkedStack()
        self.redo_stack = LinkedStack()

    def save_state(self, memento):
        self.undo_stack.push(memento)
        self.redo_stack.clear()

    def undo(self, current_state):
        if self.undo_stack.is_empty():
            return None

        self.redo_stack.push(current_state)
        return self.undo_stack.pop()

    def redo(self, current_state):
        if self.redo_stack.is_empty():
            return None

        self.undo_stack.push(current_state)
        return self.redo_stack.pop()
