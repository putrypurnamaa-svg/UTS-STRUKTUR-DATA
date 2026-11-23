
import time
import tracemalloc
import matplotlib.pyplot as plt

from linked_stack import LinkedStack
from undo_redo import HistoryManager


# ==========================================
# 1. DATA PENGUJIAN
# ==========================================

JUMLAH_DATA = [100, 250, 500, 750, 1000]

# Menyimpan hasil pengujian
waktu_undo = []
waktu_redo = []

memori_undo = []
memori_redo = []

waktu_push = []
waktu_pop = []

memori_push = []
memori_pop = []


# ==========================================
# 2. FUNGSI PENGUKURAN WAKTU DAN MEMORI
# ==========================================

def ukur_performa(fungsi):

    tracemalloc.start()

    waktu_mulai = time.perf_counter()

    fungsi()

    waktu_selesai = time.perf_counter()

    memori_sekarang, memori_puncak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    waktu = waktu_selesai - waktu_mulai
    memori = memori_puncak / 1024

    return waktu, memori


# ==========================================
# 3. PENGUJIAN SETIAP JUMLAH DATA
# ==========================================

def pengujian_performa(jumlah_data):

    print("\n======================================")
    print(f" PENGUJIAN {jumlah_data} DATA")
    print("======================================")

    # --------------------------------------
    # A. PENGUJIAN PENAMBAHAN DATA (PUSH)
    # --------------------------------------

    stack = LinkedStack()

    def tambah_data():
        for i in range(jumlah_data):
            stack.push(f"Data {i + 1}")

    waktu_p, memori_p = ukur_performa(tambah_data)

    waktu_push.append(waktu_p)
    memori_push.append(memori_p)

    print("\nPENGUJIAN PUSH")
    print("Jumlah data ditambahkan:", stack.size())
    print("Data teratas:", stack.peek())
    print(f"Waktu: {waktu_p:.6f} detik")
    print(f"Memori puncak: {memori_p:.2f} KB")

    # --------------------------------------
    # B. PENGUJIAN PENGHAPUSAN DATA (POP)
    # --------------------------------------

    def hapus_data():
        for i in range(jumlah_data):
            stack.pop()

    waktu_h, memori_h = ukur_performa(hapus_data)

    waktu_pop.append(waktu_h)
    memori_pop.append(memori_h)

    print("\nPENGUJIAN POP")
    print("Jumlah data dihapus:", jumlah_data)
    print("Sisa data:", stack.size())
    print("Apakah stack kosong?", stack.is_empty())
    print(f"Waktu: {waktu_h:.6f} detik")
    print(f"Memori puncak: {memori_h:.2f} KB")

    # --------------------------------------
    # C. MENYIAPKAN DATA UNDO DAN REDO
    # --------------------------------------

    history = HistoryManager()
    teks = ""

    for i in range(jumlah_data):
        history.save_state(teks)
        teks = f"Teks versi {i + 1}"

    # --------------------------------------
    # D. PENGUJIAN UNDO
    # --------------------------------------

    def jalankan_undo():
        nonlocal teks

        for i in range(jumlah_data):
            teks = history.undo(teks)

    waktu_u, memori_u = ukur_performa(jalankan_undo)

    waktu_undo.append(waktu_u)
    memori_undo.append(memori_u)

    print("\nPENGUJIAN UNDO")
    print("Teks setelah Undo:", teks)
    print(f"Waktu: {waktu_u:.6f} detik")
    print(f"Memori puncak: {memori_u:.2f} KB")

    # --------------------------------------
    # E. PENGUJIAN REDO
    # --------------------------------------

    def jalankan_redo():
        nonlocal teks

        for i in range(jumlah_data):
            teks = history.redo(teks)

    waktu_r, memori_r = ukur_performa(jalankan_redo)

    waktu_redo.append(waktu_r)
    memori_redo.append(memori_r)

    print("\nPENGUJIAN REDO")
    print("Teks setelah Redo:", teks)
    print(f"Waktu: {waktu_r:.6f} detik")
    print(f"Memori puncak: {memori_r:.2f} KB")


# ==========================================
# 4. MENJALANKAN PENGUJIAN
# ==========================================

print("======================================")
print("   PENGUJIAN PERFORMA LINKED STACK")
print("       FITUR UNDO DAN REDO")
print("======================================")

for jumlah in JUMLAH_DATA:
    pengujian_performa(jumlah)


# ==========================================
# 5. MENAMPILKAN TABEL HASIL
# ==========================================

print("\n======================================")
print("          RINGKASAN HASIL")
print("======================================")

print(
    f"{'Data':<10}"
    f"{'Undo (s)':<15}"
    f"{'Redo (s)':<15}"
    f"{'Undo (KB)':<15}"
    f"{'Redo (KB)':<15}"
)

for i in range(len(JUMLAH_DATA)):

    print(
        f"{JUMLAH_DATA[i]:<10}"
        f"{waktu_undo[i]:<15.6f}"
        f"{waktu_redo[i]:<15.6f}"
        f"{memori_undo[i]:<15.2f}"
        f"{memori_redo[i]:<15.2f}"
    )


# ==========================================
# 6. GRAFIK WAKTU EKSEKUSI
# ==========================================

plt.figure(figsize=(9, 5))

plt.plot(
    JUMLAH_DATA,
    waktu_undo,
    marker="o",
    label="Undo"
)

plt.plot(
    JUMLAH_DATA,
    waktu_redo,
    marker="o",
    label="Redo"
)

plt.title("Perbandingan Waktu Eksekusi Undo dan Redo")
plt.xlabel("Jumlah Data")
plt.ylabel("Waktu Eksekusi (Detik)")
plt.xticks(JUMLAH_DATA)
plt.legend()
plt.grid(True)

plt.savefig("grafik_waktu.png", dpi=300, bbox_inches="tight")

plt.show()


# ==========================================
# 7. GRAFIK PENGGUNAAN MEMORI
# ==========================================

plt.figure(figsize=(9, 5))

plt.plot(
    JUMLAH_DATA,
    memori_undo,
    marker="o",
    label="Undo"
)

plt.plot(
    JUMLAH_DATA,
    memori_redo,
    marker="o",
    label="Redo"
)

plt.title("Perbandingan Penggunaan Memori Undo dan Redo")
plt.xlabel("Jumlah Data")
plt.ylabel("Memori Puncak (KB)")
plt.xticks(JUMLAH_DATA)
plt.legend()
plt.grid(True)

plt.savefig("grafik_memori.png", dpi=300, bbox_inches="tight")

plt.show()


# ==========================================
# 8. GRAFIK TAMBAHAN PUSH DAN POP
# ==========================================

plt.figure(figsize=(9, 5))

plt.plot(
    JUMLAH_DATA,
    waktu_push,
    marker="o",
    label="Push"
)

plt.plot(
    JUMLAH_DATA,
    waktu_pop,
    marker="o",
    label="Pop"
)

plt.title("Perbandingan Waktu Penambahan dan Penghapusan Data")
plt.xlabel("Jumlah Data")
plt.ylabel("Waktu Eksekusi (Detik)")
plt.xticks(JUMLAH_DATA)
plt.legend()
plt.grid(True)

plt.savefig("grafik_push_pop.png", dpi=300, bbox_inches="tight")

plt.show()


print("\n======================================")
print("       SEMUA PENGUJIAN SELESAI")
print("======================================")
print("Grafik berhasil disimpan:")
print("1. grafik_waktu.png")
print("2. grafik_memori.png")
print("3. grafik_push_pop.png")
