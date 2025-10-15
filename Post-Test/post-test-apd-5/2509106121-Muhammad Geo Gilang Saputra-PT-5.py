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
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def register():
    clear()
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
    
def login():
    clear()
    print("=== LOGIN COFFEE SHOP ===")
    username = input("Username: ")
    password = input("Password: ")

    for u in users:
        if u[0] == username and u[1] == password:
            print(f"\n✅ Selamat datang, {username}!")
            input("\nTekan Enter untuk lanjut...")
            return u[2]  
    print("\n❌ Username atau password salah!")
    input("\nTekan Enter untuk ulangi...")
    return None

def menu_admin():
    while True:
        clear()
        print("=== MENU ADMIN COFFEE SHOP ===")
        print("1. Lihat Menu")
        print("2. Tambah Menu (Create)")
        print("3. Ubah Menu (Update)")
        print("4. Hapus Menu (Delete)")
        print("5. Logout")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            read_menu()
        elif pilih == "2":
            create_menu()
        elif pilih == "3":
            update_menu()
        elif pilih == "4":
            delete_menu()
        elif pilih == "5":
            break
        else:
            print("⚠️ Pilihan tidak valid!")
            input("\nTekan Enter untuk lanjut...")

def menu_user():
    while True:
        clear()
        print("=== MENU PENGGUNA COFFEE SHOP ===")
        print("1. Lihat Menu")
        print("2. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            read_menu()
        elif pilih == "2":
            break
        else:
            print("⚠️ Pilihan tidak valid!")
            input("\nTekan Enter untuk lanjut...")

def read_menu():
    clear()
    print("=== DAFTAR MENU COFFEE SHOP ===")
    if len(menu_coffee) == 0:
        print("Belum ada menu tersedia.")
    else:
        for i, item in enumerate(menu_coffee):
            print(f"{i+1}. {item[0]} - Rp{item[1]}")
    input("\nTekan Enter untuk kembali...")

def create_menu():
    clear()
    print("=== TAMBAH MENU BARU ===")
    nama = input("Nama kopi: ")
    harga = input("Harga: ")
    if harga.isdigit():
        menu_coffee.append([nama, int(harga)])
        print("\n✅ Menu berhasil ditambahkan!")
    else:
        print("\n⚠️ Harga harus berupa angka!")
    input("\nTekan Enter untuk kembali...")

def update_menu():
    clear()
    print("=== UBAH MENU ===")
    read_menu()
    idx = input("Masukkan nomor menu yang ingin diubah: ")
    if idx.isdigit():
        idx = int(idx) - 1
        if idx >= 0 and idx < len(menu_coffee):
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

def delete_menu():
    clear()
    print("=== HAPUS MENU ===")
    read_menu()
    idx = input("Masukkan nomor menu yang ingin dihapus: ")
    if idx.isdigit():
        idx = int(idx) - 1
        if idx >= 0 and idx < len(menu_coffee):
            del menu_coffee[idx]
            print("\n✅ Menu berhasil dihapus!")
        else:
            print("\n⚠️ Nomor menu tidak ditemukan!")
    else:
        print("\n⚠️ Input tidak valid!")
    input("\nTekan Enter untuk kembali...") 

while True:
    clear()
    print("=== SISTEM MANAJEMEN COFFEE SHOP ☕ ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        role = login()
        if role == "admin":
            menu_admin()
        elif role == "user":
            menu_user()
    elif pilih == "2":
        register()
    elif pilih == "3":
        clear()
        print("Terima kasih telah menggunakan sistem kami ☕")
        break
    else:
        print("⚠️ Pilihan tidak valid!")
        input("\nTekan Enter untuk lanjut...")
