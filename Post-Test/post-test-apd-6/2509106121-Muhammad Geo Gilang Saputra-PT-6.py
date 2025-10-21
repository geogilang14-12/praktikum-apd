import os

users = {
    "admin": {"password": "111", "role": "admin"},
    "user": {"password": "123", "role": "user"}
}

menu_coffee = {
    1: {"nama": "Americano", "harga": 15000},
    2: {"nama": "Latte", "harga": 20000},
    3: {"nama": "Cappuccino", "harga": 18000}
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print("=== SISTEM MANAJEMEN COFFEE SHOP ☕ ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "2":
        clear()
        print("=== REGISTER AKUN BARU ===")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")

        if username in users:
            print("\nUsername sudah terdaftar!")
        else:
            users[username] = {"password": password, "role": "user"}
            print("\n Akun berhasil dibuat!")

        input("\nTekan Enter untuk kembali...")

    elif pilih == "1":
        clear()
        print("=== LOGIN COFFEE SHOP ===")
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"\nSelamat datang, {username}!")
            input("\nTekan Enter untuk lanjut...")

            if role == "admin":
                while True:
                    clear()
                    print("=== MENU ADMIN COFFEE SHOP ===")
                    print("1. Lihat Menu")
                    print("2. Tambah Menu")
                    print("3. Ubah Menu")
                    print("4. Hapus Menu")
                    print("5. Logout")
                    pilih_admin = input("Pilih menu: ")

                    if pilih_admin == "1":
                        clear()
                        print("=== DAFTAR MENU COFFEE SHOP ===")
                        if len(menu_coffee) == 0:
                            print("Belum ada menu tersedia.")
                        else:
                            for i, data in menu_coffee.items():
                                print(f"{i}. {data['nama']} - Rp{data['harga']}")
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_admin == "2":
                        clear()
                        print("=== TAMBAH MENU BARU ===")
                        nama = input("Nama kopi: ")
                        harga = input("Harga: ")
                        if harga.isdigit():
                            id_baru = max(menu_coffee.keys()) + 1 if menu_coffee else 1
                            menu_coffee[id_baru] = {"nama": nama, "harga": int(harga)}
                            print("\nMenu berhasil ditambahkan!")
                        else:
                            print("\nHarga harus berupa angka!")
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_admin == "3":
                        clear()
                        print("=== UBAH MENU ===")
                        if len(menu_coffee) == 0:
                            print("Belum ada menu yang bisa diubah.")
                        else:
                            for i, data in menu_coffee.items():
                                print(f"{i}. {data['nama']} - Rp{data['harga']}")
                            idx = input("Masukkan nomor menu yang ingin diubah: ")
                            if idx.isdigit():
                                idx = int(idx)
                                if idx in menu_coffee:
                                    nama = input("Nama baru: ")
                                    harga = input("Harga baru: ")
                                    if harga.isdigit():
                                        menu_coffee[idx] = {"nama": nama, "harga": int(harga)}
                                        print("\nMenu berhasil diubah!")
                                    else:
                                        print("\nHarga harus berupa angka!")
                                else:
                                    print("\nNomor menu tidak ditemukan!")
                            else:
                                print("\nInput tidak valid!")
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_admin == "4":
                        clear()
                        print("=== HAPUS MENU ===")
                        if len(menu_coffee) == 0:
                            print("Tidak ada menu untuk dihapus.")
                        else:
                            for i, data in menu_coffee.items():
                                print(f"{i}. {data['nama']} - Rp{data['harga']}")
                            idx = input("Masukkan nomor menu yang ingin dihapus: ")
                            if idx.isdigit():
                                idx = int(idx)
                                if idx in menu_coffee:
                                    del menu_coffee[idx]
                                    print("\nMenu berhasil dihapus!")
                                else:
                                    print("\nNomor menu tidak ditemukan!")
                            else:
                                print("\nInput tidak valid!")
                        input("\nTekan Enter untuk kembali...")

                    # Logout
                    elif pilih_admin == "5":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("\nTekan Enter untuk lanjut...")

            elif role == "user":
                while True:
                    clear()
                    print("=== MENU PENGGUNA COFFEE SHOP ===")
                    print("1. Lihat Menu")
                    print("2. Logout")
                    pilih_user = input("Pilih menu: ")

                    if pilih_user == "1":
                        clear()
                        print("=== DAFTAR MENU COFFEE SHOP ===")
                        if len(menu_coffee) == 0:
                            print("Belum ada menu tersedia.")
                        else:
                            for i, data in menu_coffee.items():
                                print(f"{i}. {data['nama']} - Rp{data['harga']}")
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_user == "2":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("\nTekan Enter untuk lanjut...")

        else:
            print("\nUsername atau password salah!")
            input("\nTekan Enter untuk ulangi...")

    elif pilih == "3":
        clear()
        print("Terima kasih telah menggunakan sistem kami ☕")
        break

    else:
        print("⚠️ Pilihan tidak valid!")
        input("\nTekan Enter untuk lanjut...")
