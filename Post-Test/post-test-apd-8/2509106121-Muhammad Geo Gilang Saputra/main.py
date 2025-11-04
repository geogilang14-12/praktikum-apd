from util import clear, header
from auth import login, register
from menu import tampilkan_menu, tambah_menu, ubah_menu, hapus_menu
from transaksi import pesan_kopi, lihat_total

while True:
    clear()
    header("SISTEM MANAJEMEN COFFEE SHOP ☕")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        role, username = login()
        if role == "admin":
            while True:
                clear()
                header("MENU ADMIN")
                print("1. Lihat Menu")
                print("2. Tambah Menu")
                print("3. Ubah Menu")
                print("4. Hapus Menu")
                print("5. Lihat Total Transaksi")
                print("6. Logout")
                p = input("Pilih menu: ")
                if p == "1": tampilkan_menu(); input()
                elif p == "2": tambah_menu()
                elif p == "3": ubah_menu()
                elif p == "4": hapus_menu()
                elif p == "5": lihat_total()
                elif p == "6": break
        elif role == "user":
            while True:
                clear()
                header(f"MENU USER ({username})")
                print("1. Lihat Menu")
                print("2. Pesan Kopi")
                print("3. Logout")
                p = input("Pilih menu: ")
                if p == "1": tampilkan_menu(); input()
                elif p == "2": pesan_kopi()
                elif p == "3": break

    elif pilih == "2":
        register()

    elif pilih == "3":
        clear()
        print("Terima kasih telah menggunakan sistem kami ☕")
        break
