from util import header

users = {
    "admin": {"password": "111", "role": "admin"},
    "user": {"password": "123", "role": "user"}
}

def register():
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
    input("\nTekan Enter untuk kembali...")

def login():
    header("LOGIN COFFEE SHOP")
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]["password"] == password:
        print(f"\nSelamat datang, {username}!")
        input("\nTekan Enter untuk lanjut...")
        return users[username]["role"], username
    else:
        print("\n⚠️ Username atau password salah!")
        input("\nTekan Enter untuk ulangi...")
        return None, None
