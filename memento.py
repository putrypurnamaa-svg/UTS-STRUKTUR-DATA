class Memento:
    """Menyimpan kondisi teks untuk Undo dan Redo."""

    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state