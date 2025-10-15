# praktikum = ["Mahasiswa", 20, True, 45.10, ['APD',25]]

# print(praktikum[4][1])

# # list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# # Tambahkan Web
# studyclub.insert(1,"Web")
# print(studyclub)
# # output
# ['Data Science', 'Robotics', 'Multimedia', 'Network', 'Web']


# # list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# print(studyclub)
# # Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
# studyclub[2] = "AI"
# print(studyclub)
# # output awal
# ['Data Science', 'Robotics', 'Multimedia', 'Network']
# # output sesudah
# ['Data Science', 'Robotics', 'AI', 'Network']


# # list awal
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # menghapus elemen pada indeks ke-2, yakni "Kalkulus"
# del matakuliah[2]
# print(matakuliah)
# # output awal
# ['PTI', 'APD', 'Kalkulus', 'Diskrit']
# # output sesudah
# ['PTI', 'APD', 'Diskrit']


# # list awal
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # menghapus elemen dengan nilai "Kalkulus"
# matakuliah.remove('APD')
# print(matakuliah)


# # list awal
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
# sampah = matakuliah.pop(2)
# print(matakuliah)
# print(sampah)


# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# 'Orsikom','Basis Data']
# # Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
# print(matakuliah[::2])


# a = [1, 2, 3]
# b = [4, 5, 6]
# # menggabungkan kedua list dengan operator (+)
# c = a + b
# print(c)


# a = ["teknik", "informatika"]
# # mengulang isi list dengan operator (*) sebanyak 3 kali
# c = a*3
# print(c)


# kelas = [
# ["Ridho", "Lian", "Nabil"],
# ["Daffa", "Dante", "Santoso"],
# ["Pernanda", "Riyadi", "Ahnaf"],
# ]
# # Memanggil elemen "Santoso"

# print(kelas[2][2])


# mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# # perulangan for untuk mendapatkan semua elemen
# for i in mahasiswa:
#     print( i)
#     for j in i :
#         print (j)


# #mendefinisikan tuple
# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))

# anggota = list (anggota)

# print (anggota)

# anggota = tuple 



# # tuple
# tugas = ('rangkuman', 'arduino','scrapping')
# # beri variabel setiap values
# (p, orsikom, basisdata) = tugas
# print(p)
# print(orsikom)
# print(basisdata)
# # output
# # rangkuman
# # Arduino
# # scrapping



# # tuple
# barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
# # beri variabel setiap values
# (segitiga, bulat, *kotak) = barang
# print(segitiga)
# print(bulat)
# print(kotak[0])
# # output
# # triangle
# # bola
# # ['meja', 'handphone', 'televisi']


mahasiswa = [[" ",""],["",""],("","")]

