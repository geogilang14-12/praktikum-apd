# angka_ganjil = {1, 3, 5, 7, 9}

# # for angka in angka_ganjil:
# #     print (angka)
# #     inputtambah = input ("tambah angka: ")
# #     angka_ganjil.add(inputtambah)
# #     print(angka_ganjil)

# angka_ganjil.remove (1)
# print(angka_ganjil)

# kelas = {
#     "nama" : "ridho"
#     "nama" : "geo"
# }


# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }
# print(Daftar_buku["Buku1"])
# print(Daftar_buku)


# Biodata = { 
# "Nama" : "Ananda Daffa Harahap", 
# "NIM" : 2409106050, 
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"], 
# "Mahasiswa_Aktif" : True, 
# "Social Media" : {
#     "Instagram" : "daffahrhap" 
#       } 
# }

# print(f"nama saya adalah {Biodata["Nama"]}") 
# print(f"Instagram : {Biodata['Social Media']['Instagram']}") 

# print("")
 
# print(f"nama saya adalah {Biodata.get("Nama")}") 
# print(Biodata.get("Nama"))

# print(Biodata.get("Nama")) 
# print(Biodata.get("Alamat")) 
# print(Biodata.get("Alamat", "Key ini tidak ada")) 
 
# Ananda Daffa Harahap 
# None 
# Key tersebut tidak ada


# Nilai = { 
#     "Matematika": 80, 
#     "B. Indonesia": 90, 
#      "B. Inggris": 81, 
#     "Kimia": 78, 
#     "Fisika": 80 
# } 
 
# # Tanpa menggunakan items() 
# for i in Nilai: 
#     print(i) 
 
# print("")  # pemisah 
 
# # Menggunakan items() 
# for key, Value in Nilai.items(): 
#     print(f"Nilai {key} anda adalah {Value}") 
 
# # output 
# Matematika 
# B. Indonesia 
# B. Inggris 
# Kimia 
# Fisika 
 
# Nilai Matematika anda adalah 80 
# Nilai B. Indonesia anda adalah 90 
# Nilai B. Inggris anda adalah 81 
# Nilai Kimia anda adalah 78 
# Nilai Fisika anda adalah 80


# Film = { 
# "Avenger Endgame" : "Action", 
# "Sherlock Holmes" : "Mystery", 
# "The Conjuring" : "Horror" 
# } 
# #Sebelum Ditambah 
# print(Film) 
 
# Film["Zombielandsd"] = "Comedy" 
# Film.update({"Hours" : "Thriller"}) 

# #Setelah Ditambah 
# print(Film) 
 
# #Sebelum Ditambah 
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
# 'The Conjuring': 'Horror'} 
 
# #Setelah Ditambah 
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
# 'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours': 
# 'Thriller'}

# data = { 
# "Nama" : "Daffa", 
# "Umur" : 19, 
# "Jurusan" : "Informatika" 
# } 
# #Sebelum Dihapus 
# print(data) 
 
# del data["Nama"] 
 
# #Setelah diubah
# print(data) 
 
# #memanggil data yang telah dihapus 
# print(data.get("Nama")) 
 
# {'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
 
# {'Umur': 19, 'Jurusan': 'Informatika'} 
 
# None

# cache = data.pop("Nama")


# data = { 
# "Nama" : "Daffa", 
# "Umur" : 19, 
# "Jurusan" : "Informatika" 
# } 
 
# #Sebelum Dihapus 
# print(data) 
 
# data.clear() 
 
# #Setelah dihapus 
# print(data) 
 
# {'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
 
# {}

# data = { 
# "Nama" : "Daffa", 
# "Umur" : 19, 
# "Jurusan" : "Informatika" 
# }

# print("Jumlah Data = ", len(data)) 
 
# JumlahData = 3

# key = "apel", "jeruk", "mangga" 
# value = 1, 2, 3 
# buah = dict.fromkeys(key, value) 
# print(buah) 

Nilai = { 
"Matematika" : 80, 
"B. Indonesia" : 90, 
"B. Inggris" : 81 
} 
 
#sebelum Setdefault 
print(Nilai) 
 
print("") 
 
#menggunakan setdefault 
print("Nilai : ", Nilai.setdefault("Kimia", 70)) 
 
print("Nilai")