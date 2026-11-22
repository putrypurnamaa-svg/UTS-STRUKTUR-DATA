
class Node:
    """
    Node untuk Linked Stack.
    Setiap node menyimpan data dan
    referensi ke node berikutnya.
    """

    def __init__(self, data):
        self.data = data
        self.next = None
