import os

# =============================
# VARIABEL GLOBAL
# =============================
users = {
    "admin": {"password": "111", "role": "admin"},
    "user": {"password": "123", "role": "user"}
}

menu_coffee = {
    1: {"nama": "Americano", "harga": 15000},
    2: {"nama": "Latte", "harga": 20000},
    3: {"nama": "Cappuccino", "harga": 18000}
}

transaksi_total = 0  # variabel global tambahan

# =============================
# PROSEDUR
# =============================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(teks):
    print("=" * 40)
    print(teks.center(40))
    print("=" * 40)

# =============================
# FUNGSI TANPA PARAMETER
# =============================
def tampilkan_menu():
    """Menampilkan daftar menu kopi"""
    header("DAFTAR MENU COFFEE SHOP")
    if not menu_coffee:
        print("Belum ada menu tersedia.")
    else:
        for i, data in menu_coffee.items():
            print(f"{i}. {data['nama']} - Rp{data['harga']}")
    print("=" * 40)

def hitung_total():
    """Menampilkan total transaksi global"""
    print(f"Total transaksi saat ini: Rp{transaksi_total}")

# =============================
# FUNGSI DENGAN PARAMETER
# =============================
def tambah_menu(nama, harga):
    """Menambah menu kopi baru"""
    try:
        if not nama.strip():
            raise ValueError("Nama menu tidak boleh kosong!")
        if harga <= 0:
            raise ValueError("Harga harus lebih besar dari 0!")
        id_baru = max(menu_coffee.keys()) + 1 if menu_coffee else 1
        menu_coffee[id_baru] = {"nama": nama, "harga": harga}
        print("✅ Menu berhasil ditambahkan!")
    except ValueError as e:
        print(f"⚠️ Error: {e}")

def pesan_kopi(jumlah):
    """Fungsi rekursif untuk menghitung total harga pesanan"""
    if jumlah == 0:
        return 0
    else:
        tampilkan_menu()
        try:
            pilih = int(input("Masukkan nomor kopi yang ingin dipesan: "))
            if pilih not in menu_coffee:
                raise KeyError("Menu tidak ditemukan!")
            harga = menu_coffee[pilih]["harga"]
            print(f"Pesanan ditambahkan: {menu_coffee[pilih]['nama']} - Rp{harga}")
            return harga + pesan_kopi(jumlah - 1)
        except (ValueError, KeyError) as e:
            print(f"⚠️ {e}")
            return pesan_kopi(jumlah - 1)
        finally:
            print("Transaksi sebagian selesai.\n")

# =============================
# PROGRAM UTAMA
# =============================
while True:
    clear()
    header("SISTEM MANAJEMEN COFFEE SHOP ☕")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    # REGISTER
    if pilih == "2":
        clear()
        header("REGISTER AKUN BARU")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")

        try:
            if not username.strip():
                raise ValueError("Username tidak boleh kosong!")
            if len(password) < 3:
                raise ValueError("Password minimal 3 karakter!")
            if username in users:
                raise KeyError("Username sudah terdaftar!")

            users[username] = {"password": password, "role": "user"}
            print("\n✅ Akun berhasil dibuat!")
        except (ValueError, KeyError) as e:
            print(f"⚠️ {e}")
        finally:
            input("\nTekan Enter untuk kembali...")

    # LOGIN
    elif pilih == "1":
        clear()
        header("LOGIN COFFEE SHOP")
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"\nSelamat datang, {username}!")
            input("\nTekan Enter untuk lanjut...")

            # MENU ADMIN
            if role == "admin":
                while True:
                    clear()
                    header("MENU ADMIN COFFEE SHOP")
                    print("1. Lihat Menu")
                    print("2. Tambah Menu")
                    print("3. Ubah Menu")
                    print("4. Hapus Menu")
                    print("5. Lihat Total Transaksi")
                    print("6. Logout")
                    pilih_admin = input("Pilih menu: ")

                    # Lihat menu
                    if pilih_admin == "1":
                        clear()
                        tampilkan_menu()
                        input("\nTekan Enter untuk kembali...")

                    # Tambah menu
                    elif pilih_admin == "2":
                        clear()
                        header("TAMBAH MENU BARU")
                        nama = input("Nama kopi: ")
                        try:
                            harga = int(input("Harga: "))
                            tambah_menu(nama, harga)
                        except ValueError:
                            print("Harga harus berupa angka!")
                        input("\nTekan Enter untuk kembali...")

                    # Ubah menu
                    elif pilih_admin == "3":
                        clear()
                        header("UBAH MENU COFFEE SHOP")
                        if len(menu_coffee) == 0:
                            print("Belum ada menu yang bisa diubah.")
                        else:
                            tampilkan_menu()
                            try:
                                idx = int(input("Masukkan nomor menu yang ingin diubah: "))
                                if idx in menu_coffee:
                                    nama_baru = input("Masukkan nama baru: ")
                                    harga_baru = int(input("Masukkan harga baru: "))
                                    if not nama_baru.strip():
                                        raise ValueError("Nama tidak boleh kosong!")
                                    if harga_baru <= 0:
                                        raise ValueError("Harga harus lebih besar dari 0!")
                                    menu_coffee[idx]["nama"] = nama_baru
                                    menu_coffee[idx]["harga"] = harga_baru
                                    print("\n✅ Menu berhasil diubah!")
                                else:
                                    raise KeyError("Nomor menu tidak ditemukan!")
                            except (ValueError, KeyError) as e:
                                print(f"⚠️ {e}")
                            finally:
                                input("\nTekan Enter untuk kembali...")

                    # Hapus menu
                    elif pilih_admin == "4":
                        clear()
                        tampilkan_menu()
                        try:
                            idx = int(input("Masukkan nomor menu yang ingin dihapus: "))
                            if idx in menu_coffee:
                                del menu_coffee[idx]
                                print("Menu berhasil dihapus!")
                            else:
                                raise KeyError("Nomor menu tidak ditemukan!")
                        except (ValueError, KeyError) as e:
                            print(f"⚠️ {e}")
                        finally:
                            input("\nTekan Enter untuk kembali...")

                    # Total transaksi
                    elif pilih_admin == "5":
                        hitung_total()
                        input("\nTekan Enter untuk kembali...")

                    # Logout
                    elif pilih_admin == "6":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("\nTekan Enter untuk lanjut...")

            # MENU USER
            elif role == "user":
                while True:
                    clear()
                    header("MENU PENGGUNA COFFEE SHOP")
                    print("1. Lihat Menu")
                    print("2. Pesan Kopi")
                    print("3. Logout")
                    pilih_user = input("Pilih menu: ")

                    if pilih_user == "1":
                        clear()
                        tampilkan_menu()
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_user == "2":
                        clear()
                        try:
                            jumlah = int(input("Berapa jenis kopi yang ingin dipesan? "))
                            total = pesan_kopi(jumlah)
                            # tidak perlu global di sini
                            transaksi_total += total
                            print(f"\nTotal harga pesanan: Rp{total}")
                        except ValueError:
                            print("Input harus berupa angka!")
                        finally:
                            input("\nTekan Enter untuk kembali...")

                    elif pilih_user == "3":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("\nTekan Enter untuk lanjut...")

        else:
            print("\nUsername atau password salah!")
            input("\nTekan Enter untuk ulangi...")

    # KELUAR
    elif pilih == "3":
        clear()
        print("Terima kasih telah menggunakan sistem kami ☕")
        break

    else:
        print("⚠️ Pilihan tidak valid!")
        input("\nTekan Enter untuk lanjut...")


