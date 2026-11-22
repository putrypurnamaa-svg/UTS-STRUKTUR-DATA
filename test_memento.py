from memento import Memento

print("=== PENGUJIAN MEMENTO PATTERN ===")

# Membuat kondisi teks awal
teks_awal = "Halo"

# Menyimpan kondisi teks
memento = Memento(teks_awal)

# Mengambil kondisi teks
hasil = memento.get_state()

print("Teks awal:", teks_awal)
print("Teks yang disimpan:", hasil)

# Memeriksa hasil
if hasil == teks_awal:
    print("Pengujian BERHASIL!")
else:
    print("Pengujian GAGAL!")