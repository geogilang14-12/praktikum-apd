import os

# =======================
# DATA USER DAN MENU
# =======================
users = [["admin", "111", "admin"], ["user", "123", "user"]]
menu_coffee = [
    ["Americano", 15000],
    ["Latte", 20000],
    ["Cappuccino", 18000]
]

# =======================
# PROGRAM UTAMA
# =======================
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM MANAJEMEN COFFEE SHOP ☕ ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    # =======================
    # REGISTER
    # =======================
    if pilih == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")
        role = "user"
        found = False

        for u in users:
            if u[0] == username:
                found = True

        if found:
            print("\n⚠️ Username sudah terdaftar!")
        else:
            users.append([username, password, role])
            print("\n✅ Akun berhasil dibuat!")

        input("\nTekan Enter untuk kembali...")

    # =======================
    # LOGIN
    # =======================
    elif pilih == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN COFFEE SHOP ===")
        username = input("Username: ")
        password = input("Password: ")
        role = None

        for u in users:
            if u[0] == username and u[1] == password:
                role = u[2]

        if role is None:
            print("\n❌ Username atau password salah!")
            input("\nTekan Enter untuk ulangi...")
        else:
            print(f"\n✅ Selamat datang, {username}!")
            input("\nTekan Enter untuk lanjut...")

            # =======================
            # MENU ADMIN
            # =======================
            if role == "admin":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== MENU ADMIN COFFEE SHOP ===")
                    print("1. Lihat Menu")
                    print("2. Tambah Menu (Create)")
                    print("3. Ubah Menu (Update)")
                    print("4. Hapus Menu (Delete)")
                    print("5. Logout")
                    pilih_admin = input("Pilih menu: ")

                    # Lihat Menu
                    if pilih_admin == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR MENU COFFEE SHOP ===")
                        if len(menu_coffee) == 0:
                            print("Belum ada menu tersedia.")
                        else:
                            for i, item in enumerate(menu_coffee):
                                print(f"{i+1}. {item[0]} - Rp{item[1]}")
                        input("\nTekan Enter untuk kembali...")

                    # Tambah Menu
                    elif pilih_admin == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== TAMBAH MENU BARU ===")
                        nama = input("Nama kopi: ")
                        harga = input("Harga: ")
                        if harga.isdigit():
                            menu_coffee.append([nama, int(harga)])
                            print("\n✅ Menu berhasil ditambahkan!")
                        else:
                            print("\n⚠️ Harga harus berupa angka!")
                        input("\nTekan Enter untuk kembali...")

                    # Ubah Menu
                    elif pilih_admin == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== UBAH MENU ===")
                        if len(menu_coffee) == 0:
                            print("Belum ada menu yang bisa diubah.")
                        else:
                            for i, item in enumerate(menu_coffee):
                                print(f"{i+1}. {item[0]} - Rp{item[1]}")
                            idx = input("Masukkan nomor menu yang ingin diubah: ")
                            if idx.isdigit():
                                idx = int(idx) - 1
                                if 0 <= idx < len(menu_coffee):
                                    nama = input("Nama baru: ")
                                    harga = input("Harga baru: ")
                                    if harga.isdigit():
                                        menu_coffee[idx] = [nama, int(harga)]
                                        print("\n✅ Menu berhasil diubah!")
                                    else:
                                        print("\n⚠️ Harga harus berupa angka!")
                                else:
                                    print("\n⚠️ Nomor menu tidak ditemukan!")
                            else:
                                print("\n⚠️ Input tidak valid!")
                        input("\nTekan Enter untuk kembali...")

                    # Hapus Menu
                    elif pilih_admin == "4":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== HAPUS MENU ===")
                        if len(menu_coffee) == 0:
                            print("Tidak ada menu untuk dihapus.")
                        else:
                            for i, item in enumerate(menu_coffee):
                                print(f"{i+1}. {item[0]} - Rp{item[1]}")
                            idx = input("Masukkan nomor menu yang ingin dihapus: ")
                            if idx.isdigit():
                                idx = int(idx) - 1
                                if 0 <= idx < len(menu_coffee):
                                    del menu_coffee[idx]
                                    print("\n✅ Menu berhasil dihapus!")
                                else:
                                    print("\n⚠️ Nomor menu tidak ditemukan!")
                            else:
                                print("\n⚠️ Input tidak valid!")
                        input("\nTekan Enter untuk kembali...")

                    # Logout
                    elif pilih_admin == "5":
                        break
                    else:
                        print("⚠️ Pilihan tidak valid!")
                        input("\nTekan Enter untuk lanjut...")

            # =======================
            # MENU USER
            # =======================
            elif role == "user":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== MENU PENGGUNA COFFEE SHOP ===")
                    print("1. Lihat Menu")
                    print("2. Logout")
                    pilih_user = input("Pilih menu: ")

                    if pilih_user == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR MENU COFFEE SHOP ===")
                        if len(menu_coffee) == 0:
                            print("Belum ada menu tersedia.")
                        else:
                            for i, item in enumerate(menu_coffee):
                                print(f"{i+1}. {item[0]} - Rp{item[1]}")
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_user == "2":
                        break
                    else:
                        print("⚠️ Pilihan tidak valid!")
                        input("\nTekan Enter untuk lanjut...")

    # =======================
    # KELUAR PROGRAM
    # =======================
    elif pilih == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan sistem kami ☕")
        break

    # =======================
    # INPUT TIDAK VALID
    # =======================
    else:
        print("⚠️ Pilihan tidak valid!")
        input("\nTekan Enter untuk lanjut...")
