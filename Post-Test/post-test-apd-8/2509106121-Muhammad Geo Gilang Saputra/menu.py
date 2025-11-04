from prettytable import PrettyTable
from util import header

menu_coffee = {
    1: {"nama": "Americano", "harga": 15000},
    2: {"nama": "Latte", "harga": 20000},
    3: {"nama": "Cappuccino", "harga": 18000}
}

def tampilkan_menu():
    header("DAFTAR MENU COFFEE SHOP")
    if not menu_coffee:
        print("Belum ada menu tersedia.")
    else:
        tabel = PrettyTable(["No", "Nama Kopi", "Harga"])
        for i, data in menu_coffee.items():
            tabel.add_row([i, data["nama"], f"Rp{data['harga']:,}"])
        print(tabel)

def tambah_menu():
    header("TAMBAH MENU BARU")
    nama = input("Nama kopi: ")
    try:
        harga = int(input("Harga: "))
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong!")
        if harga <= 0:
            raise ValueError("Harga harus lebih besar dari 0!")
        id_baru = max(menu_coffee.keys()) + 1 if menu_coffee else 1
        menu_coffee[id_baru] = {"nama": nama, "harga": harga}
        print("✅ Menu berhasil ditambahkan!")
    except ValueError as e:
        print(f"⚠️ {e}")
    input("\nTekan Enter untuk kembali...")

def ubah_menu():
    tampilkan_menu()
    try:
        idx = int(input("Masukkan nomor menu yang ingin diubah: "))
        if idx in menu_coffee:
            nama_baru = input("Masukkan nama baru: ")
            harga_baru = int(input("Masukkan harga baru: "))
            menu_coffee[idx] = {"nama": nama_baru, "harga": harga_baru}
            print("✅ Menu berhasil diubah!")
        else:
            print("⚠️ Menu tidak ditemukan!")
    except ValueError:
        print("⚠️ Input tidak valid!")
    input("\nTekan Enter untuk kembali...")

def hapus_menu():
    tampilkan_menu()
    try:
        idx = int(input("Masukkan nomor menu yang ingin dihapus: "))
        if idx in menu_coffee:
            del menu_coffee[idx]
            print("✅ Menu berhasil dihapus!")
        else:
            print("⚠️ Menu tidak ditemukan!")
    except ValueError:
        print("⚠️ Input tidak valid!")
    input("\nTekan Enter untuk kembali...")
