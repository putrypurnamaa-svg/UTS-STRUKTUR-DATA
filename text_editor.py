
class TextEditor:
    """
    Mengelola isi teks pada aplikasi editor.
    """

    def __init__(self):
        self.text = ""

    def set_text(self, new_text):
        self.text = new_text

    def get_text(self):
        return self.text

    def save(self):
        from memento import Memento
        return Memento(self.text)

    def restore(self, memento):
        self.text = memento.get_state()
