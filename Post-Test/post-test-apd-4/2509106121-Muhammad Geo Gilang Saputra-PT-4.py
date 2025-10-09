print("=== Misi Pertama: Tes Konsentrasi ===")
stamina = int(input("Masukkan stamina (3 digit NIM terakhir): ")) 
chakra = 0

while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3

print(f"Chakra terkumpul: {chakra}")
print(f"Sisa stamina: {stamina}")

if chakra >= 200:
    print("Naruto berhasil menyempurnakan Rasengan!")
else:
    print("Naruto kehabisan stamina sebelum mencapai 200 chakra.")

# ---------------------------------------------------------------

print("\n=== Misi Kedua: Infiltrasi Menara ===")
tinggi_menara = int(input("Masukkan tinggi menara (2 digit NIM terakhir): "))  # 21
gulungan = 0

for meter in range(3, tinggi_menara + 1, 3):
    gulungan += 1

print(f"Jumlah gulungan informasi yang ditemukan: {gulungan}")

# ---------------------------------------------------------------

print("\n=== Misi Ketiga: Penyelidikan ===")
koridor = int(input("Masukkan jumlah koridor (digit kedua terakhir NIM): "))  # 2
intelijen = 0
perangkap = 0

for i in range(1, koridor + 1):
    print(f"\nKoridor {i}:")
    for ruang in range(1, 4):
        if ruang % 2 != 0:
            print(f"  Ruangan {ruang}: Data Intelijen ditemukan.")
            intelijen += 1
        else:
            print(f"  Ruangan {ruang}: Perangkap Peledak dijinakkan.")
            perangkap += 1

print("\n=== Hasil Akhir Misi ===")
print(f"Total Data Intelijen: {intelijen}")
print(f"Total Perangkap Peledak: {perangkap}")
print("Semua misi selesai! Naruto menunjukkan kecepatan berpikir luar biasa.")
