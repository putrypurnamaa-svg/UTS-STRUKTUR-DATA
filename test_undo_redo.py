from undo_redo import HistoryManager

print("=== PENGUJIAN UNDO DAN REDO ===")

history = HistoryManager()

# Kondisi teks awal
teks = "Halo"

# Simpan kondisi sebelum perubahan
history.save_state(teks)

# Perubahan pertama
teks = "Halo Dunia"
print("Teks sekarang:", teks)

# Undo
teks = history.undo(teks)
print("Setelah Undo:", teks)

# Redo
teks = history.redo(teks)
print("Setelah Redo:", teks)

# Pengujian hasil
if teks == "Halo Dunia":
    print("Pengujian UNDO REDO BERHASIL!")
else:
    print("Pengujian UNDO REDO GAGAL!")