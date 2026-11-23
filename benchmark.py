import time
import tracemalloc

from linked_stack import LinkedStack
from undo_redo import HistoryManager


def ukur_memori_dan_waktu(nama_pengujian, fungsi):
    tracemalloc.start()
    waktu_mulai = time.perf_counter()

    fungsi()

    waktu_selesai = time.perf_counter()
    memori_sekarang, memori_puncak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    waktu = waktu_selesai - waktu_mulai

    print(f"\nPengujian: {nama_pengujian}")
    print(f"Waktu eksekusi: {waktu:.6f} detik")
    print(f"Memori saat ini: {memori_sekarang / 1024:.2f} KB")
    print(f"Memori puncak: {memori_puncak / 1024:.2f} KB")


def pengujian_performa(jumlah_data):
    print("\n====================================")
    print(f" PENGUJIAN DENGAN {jumlah_data} DATA")
    print("====================================")

    # 1. Pengujian penambahan data
    stack = LinkedStack()

    def tambah_data():
        for i in range(jumlah_data):
            stack.push(f"Data {i + 1}")

    ukur_memori_dan_waktu("Penambahan Data (Push)", tambah_data)

    print("Jumlah data setelah ditambahkan:", stack.size())
    print("Data teratas:", stack.peek())

    # 2. Pengujian penghapusan data
    def hapus_data():
        for i in range(jumlah_data):
            stack.pop()

    ukur_memori_dan_waktu("Penghapusan Data (Pop)", hapus_data)

    print("Jumlah data setelah dihapus:", stack.size())
    print("Apakah stack kosong?", stack.is_empty())

    # 3. Pengujian Undo dan Redo
    history = HistoryManager()
    teks = ""

    def uji_undo_redo():
        nonlocal teks

        for i in range(jumlah_data):
            history.save_state(teks)
            teks = f"Teks versi {i + 1}"

        for i in range(jumlah_data):
            teks = history.undo(teks)

        for i in range(jumlah_data):
            teks = history.redo(teks)

    ukur_memori_dan_waktu("Pengujian Undo dan Redo", uji_undo_redo)

    print("Teks akhir:", teks)


if __name__ == "__main__":
    pengujian_performa(100)
    pengujian_performa(500)
    pengujian_performa(1000)
