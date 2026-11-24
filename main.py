from undo_redo import HistoryManager


def main():
    history = HistoryManager()
    teks = ""

    while True:
        print("\n================================")
        print("       APLIKASI TEXT EDITOR")
        print("          UNDO DAN REDO")
        print("================================")

        print("\nTeks saat ini:", teks)
        print("\n1. Tulis atau ubah teks")
        print("2. Undo")
        print("3. Redo")
        print("4. Keluar")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            history.save_state(teks)
            teks = input("Masukkan teks: ")
            print("Teks berhasil diubah!")

        elif pilihan == "2":
            teks = history.undo(teks)
            print("Undo berhasil!")

        elif pilihan == "3":
            teks = history.redo(teks)
            print("Redo berhasil!")

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()