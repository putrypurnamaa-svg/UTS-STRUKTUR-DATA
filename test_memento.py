
import unittest
from memento import Memento


class TestMemento(unittest.TestCase):

    def test_menyimpan_state(self):
        memento = Memento("Halo Dunia")
        self.assertEqual(memento.get_state(), "Halo Dunia")

    def test_menyimpan_teks_kosong(self):
        memento = Memento("")
        self.assertEqual(memento.get_state(), "")

    def test_menyimpan_perubahan_teks(self):
        memento = Memento("Teks awal")
        self.assertEqual(memento.get_state(), "Teks awal")


if __name__ == "__main__":
    unittest.main()
