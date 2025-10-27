# def luas_persegi(sisi):
#     luas = sisi * sisi
#     # return luas

# print ("Luas persegi :", luas_persegi(8))


# Nama = "Hambali"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

# # membuat variabel lokal
# def info():
#     Nama = "Informatika"
#     Mata_Kuliah = "Logika Informatika"

# # mengakses variabel lokal
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)

# # mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)

# # memanggil fungsi info
# info()

# def faktorial(n):
# # Basis (Base Case): Kondisi berhenti
#     if n == 1 or n == 0:
#         return 1
#     # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
#     # Memanggil fungsi
# hasil = faktorial(5)
# print(f"Hasil dari 5! adalah: {hasil}")



film = [marvel]
# Fungsi untuk menampilkan semua data
def show_data():
    if len(film) <= 0:
        print("Belum Ada data")
    else:
        print("ID | Judul Film")
    for indeks in range(len(film)):
        print(indeks, "|", film[indeks])