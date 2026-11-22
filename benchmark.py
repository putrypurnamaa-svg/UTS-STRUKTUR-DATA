import time
import tracemalloc

from undo_redo import HistoryManager


def pengujian_performa(jumlah_operasi):
    history = HistoryManager()
    teks = ""

    # Mulai menghitung penggunaan memori
    tracemalloc.start()

    # Mulai menghitung waktu
    waktu_mulai = time.perf_counter()

    # Pengujian penyimpanan teks
    for i in range(jumlah_operasi):
        history.save_state(teks)
        teks = f"Teks versi {i + 1}"

    # Pengujian Undo
    for i in range(jumlah_operasi):
        teks = history.undo(teks)

    # Pengujian Redo
    for i in range(jumlah_operasi):
        teks = history.redo(teks)

    # Selesai menghitung waktu
    waktu_selesai = time.perf_counter()

    # Mengambil penggunaan memori
    memori_sekarang, memori_puncak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Menampilkan hasil
    print("\n=== HASIL PENGUJIAN PERFORMA ===")
    print("Jumlah operasi:", jumlah_operasi)
    print(f"Waktu eksekusi: {waktu_selesai - waktu_mulai:.6f} detik")
    print(f"Memori saat ini: {memori_sekarang / 1024:.2f} KB")
    print(f"Memori puncak: {memori_puncak / 1024:.2f} KB")


if __name__ == "__main__":
    pengujian_performa(100)
    pengujian_performa(500)
    pengujian_performa(1000)
