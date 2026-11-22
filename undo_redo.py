from linked_stack import LinkedStack
from memento import Memento


class HistoryManager:
    """Mengelola riwayat Undo dan Redo."""

    def __init__(self):
        self.undo_stack = LinkedStack()
        self.redo_stack = LinkedStack()

    def save_state(self, text):
        """Menyimpan kondisi teks sebelum perubahan."""
        self.undo_stack.push(Memento(text))
        self.redo_stack.clear()

    def undo(self, current_text):
        """Mengembalikan teks ke kondisi sebelumnya."""
        if self.undo_stack.is_empty():
            return current_text

        self.redo_stack.push(Memento(current_text))
        previous = self.undo_stack.pop()

        return previous.get_state()

    def redo(self, current_text):
        """Mengembalikan teks setelah Undo."""
        if self.redo_stack.is_empty():
            return current_text

        self.undo_stack.push(Memento(current_text))
        next_state = self.redo_stack.pop()

        return next_state.get_state()