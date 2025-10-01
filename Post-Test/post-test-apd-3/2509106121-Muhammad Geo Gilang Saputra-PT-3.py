print("=== Penghitung Gaji Karyawan PT. BOM ===")
nama = input("Masukkan Nama Karyawan: ")
jabatan = input("Masukkan Jabatan Karyawan (peracik petasan/pengantar petasan): ").lower()
hari_kerja = int(input("Masukkan Jumlah Hari Kerja: "))
jam_kerja = int(input("Masukkan Jam Kerja per Hari: "))
lembur = int(input("Masukkan Jumlah Lembur: "))
bayaran_perjam = 0
bayaran_lembur = 0

if jabatan == "peracik petasan":
    if hari_kerja >= 24 and jam_kerja >= 8 and lembur >= 4:
        bayaran_perjam = 25000
        bayaran_lembur = 15000
    elif hari_kerja >= 18 and jam_kerja >= 6 and lembur >= 2:
        bayaran_perjam = 20000
        bayaran_lembur = 10000
    else:
        bayaran_perjam = 15000
        bayaran_lembur = 10000

elif jabatan == "pengantar petasan":
    if hari_kerja >= 20 and jam_kerja >= 7 and lembur >= 7:
        bayaran_perjam = 25000
        bayaran_lembur = 20000
    elif hari_kerja >= 16 and jam_kerja >= 5 and lembur >= 4:
        bayaran_perjam = 20000
        bayaran_lembur = 15000
    else:
        bayaran_perjam = 15000
        bayaran_lembur = 12000

else:
    print("Jabatan tidak dikenali. Program dihentikan.")
    exit()
total_gaji = ((bayaran_perjam * jam_kerja) * hari_kerja) + (lembur * bayaran_lembur)
print("\n=== Rincian Gaji Karyawan PT. BOM ===")
print("Nama Karyawan   :", nama)
print("Jabatan         :", jabatan)
print("Hari Kerja      :", hari_kerja)
print("Jam Kerja       :", jam_kerja, "jam")
print("Jumlah Lembur   :", lembur, "jam")
print("Bayaran per Jam : Rp", bayaran_perjam)
print("Bayaran Lembur  : Rp", bayaran_lembur)
print("Total Gaji      : Rp", total_gaji)