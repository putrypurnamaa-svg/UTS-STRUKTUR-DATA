
from text_editor import TextEditor
from history_manager import HistoryManager


def main():
    editor = TextEditor()
    history = HistoryManager()

    print("================================")
    print("     APLIKASI TEXT EDITOR")
    print("       UNDO DAN REDO")
    print("================================")

    while True:
        print("\nTeks saat ini:", editor.get_text())

        print("\nMenu:")
        print("1. Tulis atau ubah teks")
        print("2. Undo")
        print("3. Redo")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            history.save_state(editor.save())

            teks = input("Masukkan teks baru: ")
            editor.set_text(teks)

            print("Teks berhasil disimpan.")

        elif pilihan == "2":
            hasil = history.undo(editor.save())

            if hasil is None:
                print("Tidak ada riwayat Undo.")
            else:
                editor.restore(hasil)
                print("Undo berhasil.")

        elif pilihan == "3":
            hasil = history.redo(editor.save())

            if hasil is None:
                print("Tidak ada riwayat Redo.")
            else:
                editor.restore(hasil)
                print("Redo berhasil.")

        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
