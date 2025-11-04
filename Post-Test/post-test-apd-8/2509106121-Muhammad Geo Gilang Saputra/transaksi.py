from util import header
from menu import menu_coffee, tampilkan_menu
from datetime import datetime

transaksi_total = 0

def pesan_kopi():
    global transaksi_total
    tampilkan_menu()
    try:
        jumlah = int(input("Berapa jenis kopi yang ingin dipesan? "))
        total = 0
        for i in range(jumlah):
            pilih = int(input(f"Pilih kopi ke-{i+1}: "))
            if pilih in menu_coffee:
                total += menu_coffee[pilih]["harga"]
                print(f"Ditambahkan: {menu_coffee[pilih]['nama']}")
            else:
                print("⚠️ Menu tidak ditemukan!")
        transaksi_total += total
        waktu = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        print(f"\n🕒 Waktu transaksi: {waktu}")
        print(f"💰 Total harga pesanan: Rp{total:,}")
    except ValueError:
        print("⚠️ Input tidak valid!")
    input("\nTekan Enter untuk kembali...")

def lihat_total():
    print(f"\nTotal semua transaksi: Rp{transaksi_total:,}")
    input("\nTekan Enter untuk kembali...")
